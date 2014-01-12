# -*- coding: utf-8 -*-

from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import translation

from studlan.lottery.models import Lottery, LotteryParticipant, LotteryWinner
from studlan.lan.models import LAN, Attendee

def index(request):
    lans = LAN.objects.filter(end_date__gte=datetime.now())
    if not lans.count() == 1:
        return render(request, 'lottery/lottery.html', {'lan': False})
    next_lan = lans[0]
    lotteries = Lottery.objects.filter(lan=next_lan)
    lotteries_translated = []
    signed = []
    for lottery in lotteries:
        lotteries_translated.append(lottery.get_translation(language = translation.get_language()))
        signed.append(lottery.is_participating(request.user))
    return render(request, 'lottery/lottery.html', {'lan': next_lan, 'lotteries': zip(lotteries, lotteries_translated, signed)})

def sign_up(request, lottery_id):
    lottery = get_object_or_404(Lottery, pk=lottery_id)
    if lottery.registration_open:
        LotteryParticipant.objects.create(user=request.user, lottery=lottery)

    return redirect(index)

def sign_off(request, lottery_id):
    lottery = get_object_or_404(Lottery, pk=lottery_id)
    if lottery.registration_open:
        participant = get_object_or_404(LotteryParticipant, user=request.user, lottery=lottery)
        participant.delete()

    return redirect(index)
    
