# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeoPolygon'
        db.create_table('forestry_geopolygon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forestry.TypePolygon'])),
            ('forestry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forestry.Forestry'])),
            ('oid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=False, max_length=250)),
            ('area', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2)),
            ('perimetr', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2)),
            ('full_date', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_geom', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vydel', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kvartal', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('center_zoom', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('center_lon', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=25, decimal_places=7)),
            ('center_lat', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=25, decimal_places=7)),
            ('fire_able', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wood_volume_per_ha', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('class_damage', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('firedanger', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=21, decimal_places=5)),
            ('influence_probabiliti', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('firerisk', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=7, decimal_places=2)),
            ('class_risk', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('class_risk1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('class_risk2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=900913)),
        ))
        db.send_create_signal(u'forestry', ['GeoPolygon'])


    def backwards(self, orm):
        # Deleting model 'GeoPolygon'
        db.delete_table('geo_polygon')


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
        u'forestry.geopolygon': {
            'Meta': {'object_name': 'GeoPolygon', 'db_table': "'geo_polygon'"},
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

    complete_apps = ['forestry']