from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import (
    Burial, BurialSite, BurialGroup, Urn, UrnCover, GraveGood, GraveGoodOther, DeadBodyRemains,
    AnimalRemains
)


class BurialSiteAdmin(GuardedModelAdmin):
    pass


class BurialAdmin(GuardedModelAdmin):
    pass


class BurialGroupAdmin(GuardedModelAdmin):
    pass


class UrnAdmin(GuardedModelAdmin):
    pass


class UrnCoverAdmin(GuardedModelAdmin):
    pass


class GraveGoodAdmin(GuardedModelAdmin):
    pass


class GraveGoodOtherAdmin(GuardedModelAdmin):
    pass


class DeadBodyRemainsAdmin(GuardedModelAdmin):
    pass


class AnimalRemainsAdmin(GuardedModelAdmin):
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
