from modeltranslation.translator import translator, TranslationOptions
from fires.models import Rothermel, FireDetection, FireCause, ExtingCosts, FireDamage, FireWorked

class RothermelTranslationOptions(TranslationOptions):
    fields = ('veget_type',)
translator.register(Rothermel, RothermelTranslationOptions)


class FireDetectionTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(FireDetection, FireDetectionTranslationOptions)


class FireCauseTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(FireCause, FireCauseTranslationOptions)


class ExtingCostsTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(ExtingCosts, ExtingCostsTranslationOptions)


class FireDamageTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(FireDamage, FireDamageTranslationOptions)


class FireWorkedTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(FireWorked, FireWorkedTranslationOptions)