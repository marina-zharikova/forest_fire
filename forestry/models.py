from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import datetime
from forest_fire import settings
from django.contrib.gis.db import models
from simple_translation.utils import get_language_from_request
from simple_translation.translation_pool import translation_pool
from paintstore.fields import ColorPickerField
from django.utils.html import mark_safe
from fires.models import Rothermel
# Create your models here.

class ForestryGroup(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return getattr(translation_pool.annotate_with_translations(self), 'translations', []) \
           	and unicode(translation_pool.annotate_with_translations(self).translations[0]) or u'No translations'
    class Meta:
        verbose_name=_(u'Forestry group')
        verbose_name_plural=_(u'Forestry groups')


class Forestry(models.Model):
    forestry_group = models.ForeignKey(ForestryGroup)
    name = models.CharField(max_length=250,)
    def __unicode__(self):
        return getattr(translation_pool.annotate_with_translations(self), 'translations', []) \
            	and unicode(translation_pool.annotate_with_translations(self).translations[0]) or u'No translations'
    class Meta:
        verbose_name=_(u'Forestry')
        verbose_name_plural=_(u'Forestries')


class GeoKvartal(models.Model):
    forestry = models.ForeignKey(Forestry, verbose_name=_(u'Forestry name'))
    oid = models.IntegerField(default=0)
    number = models.IntegerField(verbose_name=_(u'Block number'), default=0)
    area = models.DecimalField(verbose_name=_(u'Square'), max_digits=10, decimal_places=2, default=0)
    area_count = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    perimetr = models.DecimalField(verbose_name=_(u'Perimeter'), max_digits=10, decimal_places=2, default=0)
    center_zoom = models.IntegerField(default=0)
    center_lon = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    center_lat = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    geom = models.MultiPolygonField()
    def __unicode__(self):
        return str(self.number)

    class Meta:
        verbose_name=_(u'Block')
        verbose_name_plural=_(u'Blocks')


#Polygon type
class TypePolygon(models.Model):
    rothermel = models.ForeignKey(Rothermel, blank=True, default=False)
    name = models.CharField(max_length=250, verbose_name=_(u'Polygon type'))
    is_pub = models.BooleanField(verbose_name=u'Active', default=False)
    fill_color = ColorPickerField(verbose_name=u'Filling color', blank=True, default= "#ff0000")
    border_color = ColorPickerField(verbose_name=u'Border color', blank=True, default= "#000000")
    def __unicode__(self):
        return getattr(translation_pool.annotate_with_translations(self), 'translations', []) \
            	and unicode(translation_pool.annotate_with_translations(self).translations[0]) or u'No translations'
    @property
    def fill_color_rect(self):
        if(self.fill_color):
            return mark_safe(u'<div style="width: 25px; height: 25px; background:'+unicode(self.fill_color)+u' "></div>')
        else:
            return u'not determined'
    @property
    def border_color_rect(self):
        if(self.fill_color):
            return mark_safe(u'<div style="width: 25px; height: 25px; background:'+unicode(self.border_color)+u' "></div>')
        else:
            return u'not determined'
    class Meta:
        verbose_name=_(u'Polygon type')
        verbose_name_plural=_(u'Polygon types')
        #ordering = ['id']


class GeoPolygon(models.Model):
    type = models.ForeignKey(TypePolygon, verbose_name=_(u'Type of polygon'))
    kvartal = models.ForeignKey(GeoKvartal, verbose_name=_(u'Number of block'))
    forestry = models.ForeignKey(Forestry, verbose_name=_(u'The name of forestry'))
    oid = models.IntegerField(default=0)
    name = models.CharField(max_length=250, default=False)
    area = models.DecimalField(verbose_name=_(u'Area'), max_digits=20, decimal_places=2, default=0)
    perimetr = models.DecimalField(verbose_name=_(u'Perimeter'), max_digits=20, decimal_places=2, default=0)
    full_date = models.BooleanField(default=False)
    is_geom = models.BooleanField(default=False)
    vydel = models.IntegerField(verbose_name=_(u'Number of region'), default=0)
    kvartal = models.IntegerField(verbose_name=_(u'Number of block'), default=0)
    center_zoom = models.IntegerField(default=0)
    center_lon = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    center_lat = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    fire_able = models.IntegerField(default=0)
    wood_volume_per_ha = models.DecimalField(verbose_name=_(u'The volume of woor per ha'), max_digits=12, decimal_places=2, default=0)
    class_damage = models.IntegerField(verbose_name = (u'The class of damage'), default = 0)
    firedanger = models.DecimalField(verbose_name=_(u'Fire danger'), max_digits=21, decimal_places=5, default=0)
    influence_probabiliti = models.DecimalField(verbose_name=_(u'The probability of influence'), max_digits=12, decimal_places=2, default=0)
    firerisk = models.DecimalField(verbose_name=_(u'Fire risk'), max_digits=7, decimal_places=2, default=0)
    class_risk = models.IntegerField(verbose_name = (u'The class of fire risk'), default = 0)
    class_risk1 = models.IntegerField(verbose_name = (u'The class of fire risk'), default = 0)
    class_risk2 = models.IntegerField(verbose_name = (u'The class of fire risk'), default = 0)
    geom = models.MultiPolygonField('Country Border',srid=900913)
  #  objects = models.GeoManager()
    def __unicode__(self):
        return u'BLOCK ' + unicode(self.kvartal) + u', REGION ' + unicode(self.vydel) + u'  (' + unicode(self.name) + u')'
    class Meta:
        verbose_name=_(u'Region')
        verbose_name_plural=_(u'Regions')

class ForestElement(models.Model):
    type_polygon = models.ForeignKey(TypePolygon, verbose_name=_(u'The type of region'))
    rothermel = models.ForeignKey(Rothermel, blank=True, default=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=250,default=False)
    code = models.CharField(verbose_name=_(u'Code'), max_length=5,default=False)
    geo_polygons = models.ManyToManyField(GeoPolygon, through="ForestElement2GeoPolygon")
    def __unicode__(self):
        return getattr(translation_pool.annotate_with_translations(self), 'translations', []) \
            	and unicode(translation_pool.annotate_with_translations(self).translations[0]) or u'No translations'
    class Meta:
        verbose_name=_(u'Forest element')
        verbose_name_plural=_(u'Forest elements')

class ForestElement2GeoPolygon(models.Model):
    geo_polygon = models.ForeignKey(GeoPolygon, verbose_name=_(u'Region'), default=False)
    forest_element = models.ForeignKey(ForestElement, verbose_name=_(u'Forest element'), default=False)
    age = models.IntegerField(verbose_name=_(u'Age'), default=0)
    height = models.DecimalField(verbose_name=_(u'Height'), max_digits=5, decimal_places=2, default=0)
    diameter = models.DecimalField(verbose_name=_(u'Diameter'), max_digits=5, decimal_places=2, default=0)
    wood_store = models.DecimalField(verbose_name=_(u'The volume of wood'), max_digits=5, decimal_places=2, default=0)
    percent = models.IntegerField(verbose_name=_(u'Percentage of business trees'), default=0)
    def __unicode__(self):
        return unicode(self.geo_polygon) + u'  ' + unicode(self.forest_element) or u''
    class Meta:
        verbose_name=_(u'Forest elements inside the region')
        verbose_name_plural=_(u'Forest elements inside the region')






#Types of parameters (select input)
class TypeValue(models.Model):
    name = models.CharField(verbose_name=_(u'Type of value (select, input)'), max_length=250)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name =_(u'Type of value')
        verbose_name_plural =_(u'Types of value')


class TypeParamPolygon(models.Model):
    type_reg = models.ForeignKey(TypePolygon, verbose_name=_(u'Type of region'), default=False)
    #type_value = models.ForeignKey(TypeValue, verbose_name=_(u'Type of parameter value'), null=True, default=False)
    type_value = models.ForeignKey(TypeValue, verbose_name=_(u'Type of patameter value'), null=True, default=False)
    name = models.CharField(verbose_name=_(u'Name of parameter'), max_length=250,default=False)
    value = models.CharField(verbose_name=_(u'Value'), max_length=100, default=False)
    def __unicode__(self):
        return getattr(translation_pool.annotate_with_translations(self), 'translations', []) \
            	and unicode(translation_pool.annotate_with_translations(self).translations[0]) or u'No translations'
    class Meta:
        verbose_name=_(u'Type of parameter')
        verbose_name_plural=_(u'Types of parameters')


class ParamValueSelect(models.Model):
    param = models.ForeignKey(TypeParamPolygon, default=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=250,default=False)
    def __unicode__(self):
        return getattr(translation_pool.annotate_with_translations(self), 'translations', []) \
            	and unicode(translation_pool.annotate_with_translations(self).translations[0]) or u'No translations'
    class Meta:
        verbose_name=_(u'Value of parameter for choice')
        verbose_name_plural=_(u'Values of parameter for choice')



class ValueParamPolygon(models.Model):
    type_reg = models.ForeignKey(TypePolygon,verbose_name=_(u'Type of region'),  default=False)
    region = models.ForeignKey(GeoPolygon,verbose_name=_(u'Region'),  default=False)
    type_param = models.ForeignKey(TypeParamPolygon,verbose_name=_(u'Parameter'),  default=False)
    value = models.CharField(verbose_name=_(u'Parameter value'), max_length=100)
    def __unicode__(self):
        return unicode(self.region) + u'  ' + unicode(self.type_param)+ u'  -  ' +unicode(self.value) or u''
    class Meta:
        verbose_name=_(u'Parameter value')
        verbose_name_plural=_(u'Parameter values')




