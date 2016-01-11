# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TypeParamPolygon'
        db.create_table(u'forestry_typeparampolygon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_reg', self.gf('django.db.models.fields.related.ForeignKey')(default=False, to=orm['forestry.TypePolygon'])),
            ('type_value', self.gf('django.db.models.fields.related.ForeignKey')(default=False, to=orm['forestry.TypeValue'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=False, max_length=250)),
            ('name_en', self.gf('django.db.models.fields.CharField')(default=False, max_length=250, null=True, blank=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(default=False, max_length=250, null=True, blank=True)),
            ('name_uk', self.gf('django.db.models.fields.CharField')(default=False, max_length=250, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(default=False, max_length=100)),
        ))
        db.send_create_signal(u'forestry', ['TypeParamPolygon'])


    def backwards(self, orm):
        # Deleting model 'TypeParamPolygon'
        db.delete_table(u'forestry_typeparampolygon')


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
        u'forestry.forestelement': {
            'Meta': {'object_name': 'ForestElement'},
            'code': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '5'}),
            'geo_polygons': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['forestry.GeoPolygon']", 'through': u"orm['forestry.ForestElement2GeoPolygon']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'rothermel': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.Rothermel']", 'blank': 'True'}),
            'type_polygon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forestry.TypePolygon']"})
        },
        u'forestry.forestelement2geopolygon': {
            'Meta': {'object_name': 'ForestElement2GeoPolygon'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'diameter': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'forest_element': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['forestry.ForestElement']"}),
            'geo_polygon': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['forestry.GeoPolygon']"}),
            'height': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wood_store': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'})
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
        u'forestry.typeparampolygon': {
            'Meta': {'object_name': 'TypeParamPolygon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'type_reg': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['forestry.TypePolygon']"}),
            'type_value': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['forestry.TypeValue']", 'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '100'})
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
        },
        u'forestry.typevalue': {
            'Meta': {'object_name': 'TypeValue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['forestry']