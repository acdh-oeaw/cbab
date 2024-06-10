from django.contrib import admin
from .models import (
    Burial,
    BurialSite,
    BurialGroup,
    Urn,
    UrnCover,
    GraveGood,
    GraveGoodOther,
    DeadBodyRemains,
    AnimalRemains,
)


class BurialSiteAdmin(admin.ModelAdmin):
    pass


class BurialAdmin(admin.ModelAdmin):
    pass


class BurialGroupAdmin(admin.ModelAdmin):
    pass


class UrnAdmin(admin.ModelAdmin):
    pass


class UrnCoverAdmin(admin.ModelAdmin):
    pass


class GraveGoodAdmin(admin.ModelAdmin):
    pass


class GraveGoodOtherAdmin(admin.ModelAdmin):
    pass


class DeadBodyRemainsAdmin(admin.ModelAdmin):
    pass


class AnimalRemainsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Burial, BurialAdmin)
admin.site.register(BurialSite, BurialSiteAdmin)
admin.site.register(BurialGroup, BurialGroupAdmin)
admin.site.register(Urn, UrnAdmin)
admin.site.register(UrnCover, UrnCoverAdmin)
admin.site.register(GraveGood, GraveGoodAdmin)
admin.site.register(GraveGoodOther, GraveGoodOtherAdmin)
admin.site.register(DeadBodyRemains, DeadBodyRemainsAdmin)
admin.site.register(AnimalRemains, AnimalRemainsAdmin)
