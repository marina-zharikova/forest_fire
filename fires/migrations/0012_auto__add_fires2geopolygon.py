# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fires2GeoPolygon'
        db.create_table(u'fires_fires2geopolygon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fire', self.gf('django.db.models.fields.related.ForeignKey')(default=False, to=orm['fires.Fires'])),
            ('geo_polygon', self.gf('django.db.models.fields.related.ForeignKey')(default=False, to=orm['forestry.GeoPolygon'])),
            ('kvartal', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('vydel', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'fires', ['Fires2GeoPolygon'])


    def backwards(self, orm):
        # Deleting model 'Fires2GeoPolygon'
        db.delete_table(u'fires_fires2geopolygon')


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
        u'fires.fires': {
            'Meta': {'ordering': "['date_begin']", 'object_name': 'Fires'},
            'crowning_square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'date_begin': ('django.db.models.fields.DateTimeField', [], {'default': 'False'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'default': 'False'}),
            'date_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'exting_begin': ('django.db.models.fields.DateTimeField', [], {'default': 'False'}),
            'exting_end': ('django.db.models.fields.DateTimeField', [], {'default': 'False'}),
            'fire_cause': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.FireCause']"}),
            'fire_detection': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.FireDetection']"}),
            'forestry': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['forestry.Forestry']", 'null': 'True', 'db_column': "'forestry_id'"}),
            'ground_square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'unforest_square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'fires.fires2extingcosts': {
            'Meta': {'object_name': 'Fires2ExtingCosts'},
            'exting_costs': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.ExtingCosts']"}),
            'fire': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.Fires']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sum': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'})
        },
        u'fires.fires2firedamage': {
            'Meta': {'object_name': 'Fires2FireDamage'},
            'fire': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.Fires']"}),
            'fire_damage': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.FireDamage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sum': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'})
        },
        u'fires.fires2fireworked': {
            'Meta': {'object_name': 'Fires2FireWorked'},
            'fire': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.Fires']"}),
            'fire_worked': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.FireWorked']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'fires.fires2geopolygon': {
            'Meta': {'object_name': 'Fires2GeoPolygon'},
            'fire': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.Fires']"}),
            'geo_polygon': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['forestry.GeoPolygon']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kvartal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vydel': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
        u'forestry.geopolygon': {
            'Meta': {'object_name': 'GeoPolygon'},
            'area': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'center_lat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '25', 'decimal_places': '7'}),
            'center_lon': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '25', 'decimal_places': '7'}),
            'center_zoom': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_damage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_risk': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_risk1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_risk2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fire_able': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'firedanger': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '21', 'decimal_places': '5'}),
            'firerisk': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'forestry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forestry.Forestry']"}),
            'full_date': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '900913'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influence_probabiliti': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'is_geom': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kvartal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'oid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'perimetr': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forestry.TypePolygon']"}),
            'vydel': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wood_volume_per_ha': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'})
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

    complete_apps = ['fires']