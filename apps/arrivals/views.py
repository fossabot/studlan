# -*- encoding: utf-8 -*-

from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from apps.lan.models import Attendee, LAN, Ticket
from apps.seating.models import Seat


@permission_required('lan.register_arrivals')
def home(request):
    lans = LAN.objects.filter(end_date__gte=datetime.now())
    if lans.count() == 1:
        return redirect('arrivals', lan_id=lans[0].id)
    else:
        lans = LAN.objects.all()

    return render(request, 'arrivals/home.html', {'lans': lans})


@ensure_csrf_cookie
@permission_required('lan.register_arrivals')
def arrivals(request, lan_id):
    lan = get_object_or_404(LAN, pk=lan_id)
    total_paid_count = 0
    users_set = set()

    # Attendees (incl. paid and arrived)
    attendees = Attendee.objects.filter(lan=lan)
    users_set.update(map(lambda o: o.user, attendees))
    paid_users = map(lambda d: d['user'], attendees.filter(has_paid=True).values('user'))
    total_paid_count += len(paid_users)
    arrived_users = map(lambda d: d['user'], attendees.filter(arrived=True).values('user'))

    # Tickets
    tickets = Ticket.objects.filter(ticket_type__lan=lan)
    user_tickets = {}
    for serial_user in tickets.values('user').distinct():
        user = tickets.filter(user=serial_user['user'])[0].user
        users_set.add(user)
        user_tickets[user] = tickets.filter(user=user)
        total_paid_count += len(user_tickets[user])

    # Seats
    seats = Seat.objects.filter(user__isnull=False, seating__lan=lan)
    user_seats = {}
    for serial_user in seats.values('user').distinct():
        user = seats.filter(user=serial_user['user'])[0].user
        users_set.add(user)
        user_seats[user] = seats.filter(user=user)
        user_seats_count = len(user_seats[user])

    # Users
    users = sorted(list(users_set), key=lambda user: user.username)

    breadcrumbs = (
        (lan, reverse('lan_details', kwargs={'lan_id': lan.id})), (_(u'Arrivals'), ''),
    )
    context = {
        'breadcrumbs': breadcrumbs,
        'lan': lan,
        'users': users,
        'total_paid_count': total_paid_count,
        'attendee_count': attendees.count(),
        'paid_users': paid_users,
        'arrived_users': arrived_users,
        'user_seats': user_seats,
        'user_seats_count': user_seats_count,
        'user_tickets': user_tickets,
    }

    return render(request, 'arrivals/arrivals.html', context)


@require_POST
@permission_required('lan.register_arrivals')
def toggle(request, lan_id):
    username = request.POST.get('username')
    toggle_type = request.POST.get('type')
    previous_value = request.POST.get('prev')

    lan = get_object_or_404(LAN, pk=lan_id)
    user = get_object_or_404(User, username=username)
    attendee = get_object_or_404(Attendee, lan=lan, user=user)

    if int(toggle_type) == 0:
        attendee.has_paid = flip_string_bool(previous_value)
    elif int(toggle_type) == 1:
        attendee.arrived = flip_string_bool(previous_value)
    else:
        return HttpResponseBadRequest()

    attendee.save()

    return HttpResponse()


def flip_string_bool(val):
    if val == 'True':
        return False
    elif val == 'False':
        return True
