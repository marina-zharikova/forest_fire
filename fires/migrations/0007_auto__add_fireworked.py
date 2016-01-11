# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FireWorked'
        db.create_table(u'fires_fireworked', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=False, max_length=250)),
            ('name_en', self.gf('django.db.models.fields.CharField')(default=False, max_length=250, null=True, blank=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(default=False, max_length=250, null=True, blank=True)),
            ('name_uk', self.gf('django.db.models.fields.CharField')(default=False, max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'fires', ['FireWorked'])


    def backwards(self, orm):
        # Deleting model 'FireWorked'
        db.delete_table(u'fires_fireworked')


    models = {
        u'fires.extingcosts': {
            'Meta': {'object_name': 'ExtingCosts'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'fires.firecause': {
            'Meta': {'object_name': 'FireCause'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'fires.firedamage': {
            'Meta': {'object_name': 'FireDamage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'fires.firedetection': {
            'Meta': {'object_name': 'FireDetection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'fires.fireworked': {
            'Meta': {'object_name': 'FireWorked'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'fires.rothermel': {
            'Meta': {'object_name': 'Rothermel'},
            'depth': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'h': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mf': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'mx': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'reserve': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'ro': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'se': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'st': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'tg': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'u': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'unit_area': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'veget_type': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'veget_type_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'veget_type_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'veget_type_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'veget_type_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fires']