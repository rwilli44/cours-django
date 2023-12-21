from django.contrib import admin
from .models import Animal, Keeper, Species, Zone

# Register your models here.


class AnimalAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "species", "diet", "weight", "zone")
    list_filter = ("name", "species", "zone")
    search_fields = ("name",)


admin.site.register(Animal, AnimalAdmin)


class KeeperAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "hire_date",
    )
    list_filter = ("zones",)
    search_fields = ("name",)


admin.site.register(Keeper, KeeperAdmin)


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "conservation")
    list_filter = ("conservation",)
    search_fields = ("name",)


admin.site.register(Species, SpeciesAdmin)


class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "climate", "area")
    list_filter = ("climate", "area")
    search_fields = ("name",)


admin.site.register(Zone, ZoneAdmin)
