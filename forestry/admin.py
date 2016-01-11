from django.contrib import admin
from forestry.models import ForestryGroup, Forestry, TypePolygon, GeoKvartal, GeoPolygon, ForestElement, ForestElement2GeoPolygon, TypeValue, TypeParamPolygon, ParamValueSelect, ValueParamPolygon
from fires.models import Rothermel
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline

from modeltranslation.admin import TranslationAdmin
from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from django.conf import settings

import django_databrowse
django_databrowse.site.register(GeoKvartal)

USE_GOOGLE_TERRAIN_TILES = False

class ForestryInline(TranslationTabularInline):
    model = Forestry

class ForestryGroupAdmin(TranslationAdmin):
    list_display = ('name',)
    inlines = [ForestryInline,]
    fieldsets = [
        (u'ForestryGroups', {'fields': ('name',)})
    ]
admin.site.register(ForestryGroup, ForestryGroupAdmin)

class GeoKvartalAdmin(OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]


admin.site.register(GeoKvartal, GeoKvartalAdmin)


class TypePolygonAdmin(TranslationAdmin):
    list_display = ['__unicode__', 'fill_color', 'border_color', 'fill_color_rect', 'border_color_rect', 'is_pub']
    list_editable = ['is_pub', 'fill_color', 'border_color']
admin.site.register(TypePolygon, TypePolygonAdmin)


class GeoPolygonAdmin(OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]
    list_display = ['__unicode__', 'wood_volume_per_ha']
    search_fields = ['=kvartal', '=vydel']
    list_editable = ['wood_volume_per_ha']
admin.site.register(GeoPolygon, GeoPolygonAdmin)


class ForestElement2GeoPolygonAdmin(admin.ModelAdmin):
    list_display = ('geo_polygon', 'forest_element', 'age', 'height', 'diameter', 'wood_store', 'percent',)
    fieldsets = [
        (u'ForestElement2GeoPolygons', {'fields': ('geo_polygon', 'forest_element', 'age', 'height', 'diameter', 'wood_store', 'percent',)})
    ]
admin.site.register(ForestElement2GeoPolygon, ForestElement2GeoPolygonAdmin)


class ForestElementAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'ForestElements', {'fields': ('name',)})
    ]
admin.site.register(ForestElement, ForestElementAdmin)


class TypeValueAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'TypeValues', {'fields': ('name',)})
    ]
admin.site.register(TypeValue, TypeValueAdmin)


class TypeParamPolygonAdmin(TranslationAdmin):
    list_display = ('type_reg', 'type_value', 'name', 'value',)
    fieldsets = [
        (u'TypeParamPolygons', {'fields': ('type_reg', 'type_value', 'name', 'value',)})
    ]
admin.site.register(TypeParamPolygon, TypeParamPolygonAdmin)


class ParamValueSelectAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'ParamValueSelects', {'fields': ('name',)})
    ]
admin.site.register(ParamValueSelect, ParamValueSelectAdmin)


class ValueParamPolygonAdmin(admin.ModelAdmin):
    list_display = ('type_reg', 'region', 'type_param', 'value',)
    fieldsets = [
        (u'TypeValues', {'fields': ('type_reg', 'region', 'type_param', 'value',)})
    ]
admin.site.register(ValueParamPolygon, ValueParamPolygonAdmin)




