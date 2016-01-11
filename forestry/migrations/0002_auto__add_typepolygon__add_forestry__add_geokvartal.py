# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TypePolygon'
        db.create_table(u'forestry_typepolygon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rothermel', self.gf('django.db.models.fields.related.ForeignKey')(default=False, to=orm['fires.Rothermel'], blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('name_uk', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('is_pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fill_color', self.gf('paintstore.fields.ColorPickerField')(default='#ff0000', max_length=7, blank=True)),
            ('border_color', self.gf('paintstore.fields.ColorPickerField')(default='#000000', max_length=7, blank=True)),
        ))
        db.send_create_signal(u'forestry', ['TypePolygon'])

        # Adding model 'Forestry'
        db.create_table(u'forestry_forestry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forestry_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forestry.ForestryGroup'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('name_uk', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'forestry', ['Forestry'])

        # Adding model 'GeoKvartal'
        db.create_table(u'forestry_geokvartal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forestry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forestry.Forestry'])),
            ('oid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('area', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('area_count', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('perimetr', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('center_zoom', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('center_lon', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=7)),
            ('center_lat', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=7)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'forestry', ['GeoKvartal'])


    def backwards(self, orm):
        # Deleting model 'TypePolygon'
        db.delete_table(u'forestry_typepolygon')

        # Deleting model 'Forestry'
        db.delete_table(u'forestry_forestry')

        # Deleting model 'GeoKvartal'
        db.delete_table(u'forestry_geokvartal')


    models = {
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
            'veget_type_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'forestry.forestry': {
            'Meta': {'object_name': 'Forestry'},
            'forestry_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forestry.ForestryGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'forestry.forestrygroup': {
            'Meta': {'object_name': 'ForestryGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'forestry.geokvartal': {
            'Meta': {'object_name': 'GeoKvartal'},
            'area': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'area_count': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'center_lat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '7'}),
            'center_lon': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '7'}),
            'center_zoom': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'forestry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forestry.Forestry']"}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'oid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'perimetr': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'})
        },
        u'forestry.typepolygon': {
            'Meta': {'object_name': 'TypePolygon'},
            'border_color': ('paintstore.fields.ColorPickerField', [], {'default': "'#000000'", 'max_length': '7', 'blank': 'True'}),
            'fill_color': ('paintstore.fields.ColorPickerField', [], {'default': "'#ff0000'", 'max_length': '7', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'rothermel': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.Rothermel']", 'blank': 'True'})
        }
    }

    complete_apps = ['forestry']