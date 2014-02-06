# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lottery'
        db.create_table('lottery_lottery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lan.LAN'])),
            ('registration_open', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('lottery', ['Lottery'])

        # Adding model 'LotteryTranslation'
        db.create_table('lottery_lotterytranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['lottery.Lottery'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('lottery', ['LotteryTranslation'])

        # Adding model 'LotteryParticipant'
        db.create_table('lottery_lotteryparticipant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lottery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lottery.Lottery'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('lottery', ['LotteryParticipant'])

        # Adding model 'LotteryWinner'
        db.create_table('lottery_lotterywinner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lottery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lottery.Lottery'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('lottery', ['LotteryWinner'])


    def backwards(self, orm):
        # Deleting model 'Lottery'
        db.delete_table('lottery_lottery')

        # Deleting model 'LotteryTranslation'
        db.delete_table('lottery_lotterytranslation')

        # Deleting model 'LotteryParticipant'
        db.delete_table('lottery_lotteryparticipant')

        # Deleting model 'LotteryWinner'
        db.delete_table('lottery_lotterywinner')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lan.lan': {
            'Meta': {'ordering': "['start_date']", 'object_name': 'LAN'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lottery.lottery': {
            'Meta': {'object_name': 'Lottery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lan.LAN']"}),
            'registration_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'lottery.lotteryparticipant': {
            'Meta': {'object_name': 'LotteryParticipant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lottery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lottery.Lottery']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'lottery.lotterytranslation': {
            'Meta': {'object_name': 'LotteryTranslation'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['lottery.Lottery']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'lottery.lotterywinner': {
            'Meta': {'object_name': 'LotteryWinner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lottery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lottery.Lottery']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['lottery']