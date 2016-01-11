from django.contrib import admin
from forestry.models import ForestryGroup, Forestry, TypePolygon, GeoKvartal, GeoPolygon
from fires.models import Rothermel, FireDetection, FireCause, ExtingCosts, FireDamage, FireWorked, Fires, Fires2ExtingCosts, Fires2FireDamage, Fires2FireWorked, Fires2GeoPolygon
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline

class RothermelAdmin(TranslationAdmin):
    list_display = ('veget_type', 'reserve', 'unit_area', 'depth', 'h', 'ro', 'mf', 'st', 'se', 'u', 'tg', 'mx',)
    fieldsets = [
        (u'Rothermel', {'fields': ('veget_type', 'reserve', 'unit_area', 'depth', 'h', 'ro', 'mf', 'st', 'se', 'u', 'tg', 'mx',)})
    ]
admin.site.register(Rothermel, RothermelAdmin)


class FireDetectionAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'FireDetections', {'fields': ('name',)})
    ]
admin.site.register(FireDetection, FireDetectionAdmin)


class FireCauseAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'FireCauses', {'fields': ('name',)})
    ]
admin.site.register(FireCause, FireCauseAdmin)


class ExtingCostsAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'ExtingCosts', {'fields': ('name',)})
    ]
admin.site.register(ExtingCosts, ExtingCostsAdmin)


class FireDamageAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'FireDamages', {'fields': ('name',)})
    ]
admin.site.register(FireDamage, FireDamageAdmin)


class FiresAdmin(admin.ModelAdmin):
    list_display = ('date_begin', 'date_end', 'exting_begin', 'exting_end', 'square', 'crowning_square', 'ground_square', 'unforest_square', 'fire_detection', 'fire_cause', 'date_month',)
    fieldsets = [
        (u'Fires', {'fields': ('date_begin', 'date_end', 'exting_begin', 'exting_end', 'square', 'crowning_square', 'ground_square', 'unforest_square', 'fire_detection', 'fire_cause', 'date_month',)})
    ]
admin.site.register(Fires, FiresAdmin)


class Fires2ExtingCostsAdmin(admin.ModelAdmin):
    list_display = ('fire', 'exting_costs', 'sum',)
    fieldsets = [
        (u'Fires2ExtingCostss', {'fields': ('fire', 'exting_costs', 'sum',)})
    ]
admin.site.register(Fires2ExtingCosts, Fires2ExtingCostsAdmin)


class Fires2FireDamageAdmin(admin.ModelAdmin):
    list_display = ('fire', 'fire_damage', 'sum',)
    fieldsets = [
        (u'Fires2FireDamages', {'fields': ('fire', 'fire_damage', 'sum',)})
    ]
admin.site.register(Fires2FireDamage, Fires2FireDamageAdmin)


class Fires2FireWorkedAdmin(admin.ModelAdmin):
    list_display = ('fire', 'fire_worked', 'num',)
    fieldsets = [
        (u'Fires2FireWorkeds', {'fields': ('fire', 'fire_worked', 'num',)})
    ]
admin.site.register(Fires2FireWorked, Fires2FireWorkedAdmin)


class Fires2GeoPolygonAdmin(admin.ModelAdmin):
    list_display = ('fire', 'geo_polygon', 'kvartal', 'vydel',)
    fieldsets = [
        (u'Fires2GeoPolygons', {'fields': ('fire', 'geo_polygon', 'kvartal', 'vydel',)})
    ]
admin.site.register(Fires2GeoPolygon, Fires2GeoPolygonAdmin)