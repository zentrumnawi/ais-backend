from django.db import models
from django.utils.translation import ugettext_lazy as _
from solid_backend.content.fields import ConcatCharField, FromToConcatField
from solid_backend.content.models import BaseProfile, TreeNode

from .choices import *


class Find(BaseProfile):
    name = models.CharField(max_length=200, null=True, verbose_name=_("Name"))
    origin = models.TextField(max_length=500, blank=True, verbose_name=_("Herkunft"))
    storage = models.CharField(
        max_length=300, null=True, blank=True, verbose_name=_("Stadt, Museum/ Sammlung")
    )
    find_number = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("Fundnummer")
    )
    inven_number = models.CharField(
        max_length=200,
        default="",
        blank=True,
        null=True,
        verbose_name=_("Inventarnummer"),
    )

    source = models.CharField(max_length=300, null=True, verbose_name=_("Publikation"))

    description = models.TextField(
        max_length=400, null=True, blank=True, verbose_name=_("Beschreibung")
    )

    class Meta:
        verbose_name = _("Fundstück")
        verbose_name_plural = _("Fundstücke")


class FormalAspect(models.Model):

    shard_form = models.CharField(
        max_length=12, choices=SHARD_CHOICES, verbose_name=_("Scherbenform")
    )
    vessel_cat = models.CharField(max_length=100, verbose_name=_("Gefäßkategorie"))
    usage = models.CharField(
        max_length=19, choices=USAGE_CHOCIES, verbose_name=_("Verwendungszweck")
    )
    surface = ConcatCharField(
        max_length=400,
        concat_choices=[SURFACE_CHOICES, SURFACE_CHOICES, SURFACE_CHOICES],
        seperators=[", ", " und "],
        verbose_name=_("Oberflächenbehandlung"),
        default="",
        blank=True,
    )
    conserv = models.CharField(
        max_length=21, choices=CONSERV_CHOICES, verbose_name=_("Erhaltung")
    )
    measures = models.CharField(max_length=200, verbose_name=_("Maße (in cm)"))

    find = models.OneToOneField(
        Find,
        related_name="formal_aspect",
        on_delete=models.CASCADE,
        verbose_name=_("Fundstück"),
    )

    class Meta:
        verbose_name = _("Formale Aspekte")
        verbose_name_plural = verbose_name


class Ware(models.Model):

    manufacture = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        choices=MAN_CHOICES,
        verbose_name=_("Herstellungsart"),
    )
    brand = models.CharField(
        max_length=13,
        null=True,
        blank=True,
        choices=BRAND_CHOICES,
        verbose_name=_("Brand"),
    )
    brand_atm = models.CharField(
        max_length=21,
        null=True,
        blank=True,
        choices=BRAND_ATM_CHOICES,
        verbose_name=_("Brennatmosphäre"),
    )
    color = models.CharField(max_length=200, verbose_name=_("Farbe"))
    ornament = ConcatCharField(
        max_length=200,
        concat_choices=[ORNAM_CHOICES, ORNAM_CHOICES, ORNAM_CHOICES],
        seperators=[", ", " und "],
        default="",
        blank=True,
        verbose_name=_("Verzierungsart"),
    )
    magerungsart = models.CharField(
        max_length=52,
        null=True,
        blank=True,
        choices=MAGER_CHOICES,
        verbose_name=_("Magerungsart"),
    )
    magerungsmenge = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        choices=MAGER_MENGE_CHOICES,
        verbose_name=_("Magerungsmenge"),
    )
    magerung_size = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        choices=MAGER_SIZE_CHOICES,
        verbose_name=_("Magerungsgröße"),
    )
    magerung_dist = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=MAGER_DIST_CHOICES,
        verbose_name=_("Magerungsverteilung"),
    )
    magerung_form = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        choices=MAGER_FORM_CHOICES,
        verbose_name=_("Magerungsform"),
    )

    note = models.TextField(
        max_length=400, null=True, blank=True, verbose_name=_("Bemerkung")
    )

    find = models.OneToOneField(
        Find, related_name="ware", on_delete=models.CASCADE, verbose_name=_("Fundstück")
    )

    class Meta:
        verbose_name = _("Ware")
        verbose_name_plural = _("Waren")
