from django.db import models
from django.db.models import CASCADE, SET_NULL


# Create your models here.
class Animal(models.Model):
    CARNIVORE = "carnivore"
    OMNIVORE = "omnivore"
    HERBIVORE = "herbivore"

    DIET_CHOICES = [
        (CARNIVORE, "Carnivore"),
        (OMNIVORE, "Omnivore"),
        (HERBIVORE, "Herbivore"),
    ]

    name = models.CharField(max_length=100, help_text="Animal's name")
    birthdate = models.DateField(help_text="Animal's birthdate")
    species = models.ForeignKey(
        "Species",
        related_name="animals",
        on_delete=CASCADE,
        help_text="Animal's species",
    )
    diet = models.CharField(choices=DIET_CHOICES, help_text="Animal's diet category")
    weight = models.FloatField(help_text="Animal's weight in kilos")
    zone = models.ForeignKey(
        "Zone",
        related_name="animals",
        on_delete=CASCADE,
        help_text="Zone where the animal is kept",
    )


class Species(models.Model):
    ENDANGERED = "endangered"
    VULNERABLE = "vulnerable"
    LEAST_CONCERN = "least concern"

    CONSERVATION_STATUS = [
        (ENDANGERED, "Endangered"),
        (VULNERABLE, "Vulnerable"),
        (LEAST_CONCERN, "Least Concern"),
    ]

    name = models.CharField(max_length=100, help_text="Species' name")
    description = models.TextField(help_text="Detailed description of the species")
    conservation = models.CharField(
        choices=CONSERVATION_STATUS,
        help_text="UICN conservation status for the species",
    )

    def __str__(self):
        return f"{self.name}"


class Zone(models.Model):
    TROPICAL = "tropical"
    TEMPERATE = "temperate"
    ARCTIC = "arctic"

    CLIMATE_TYPES = [
        (TROPICAL, "Tropical"),
        (TEMPERATE, "Temperate"),
        (ARCTIC, "Arctic"),
    ]

    name = models.CharField(max_length=100, help_text="Name of the zone")
    climate = models.CharField(
        choices=CLIMATE_TYPES, help_text="Climate type of the zone"
    )
    area = models.IntegerField(help_text="The area of the zone in square meters")

    def __str__(self):
        return f"{self.name}"


class Keeper(models.Model):
    name = models.CharField(max_length=100, help_text="Keeper's name")
    hire_date = models.DateField(
        auto_now_add=True, help_text="Date the keeper was hired"
    )
    zones = models.ManyToManyField(
        Zone, related_name="keepers", help_text="Zones in which the keeper works"
    )
