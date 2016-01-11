from modeltranslation.translator import translator, TranslationOptions
from forestry.models import ForestryGroup, Forestry, TypePolygon, ForestElement, TypeParamPolygon, ParamValueSelect


class ForestryGroupTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(ForestryGroup, ForestryGroupTranslationOptions)


class ForestryTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Forestry, ForestryTranslationOptions)


class TypePolygonTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(TypePolygon, TypePolygonTranslationOptions)


class ForestElementTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(ForestElement, ForestElementTranslationOptions)


class TypeParamPolygonTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(TypeParamPolygon, TypeParamPolygonTranslationOptions)


class ParamValueSelectTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(ParamValueSelect, ParamValueSelectTranslationOptions)



