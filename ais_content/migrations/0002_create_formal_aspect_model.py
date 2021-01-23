# Generated by Django 3.0.11 on 2021-01-23 16:06

import django.db.models.deletion
import solid_backend.content.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ais_content", "0001_create_find_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormalAspect",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "shard_form",
                    models.CharField(
                        choices=[
                            ("Rand", "Rand"),
                            ("Mündung", "Mündung"),
                            ("Lippe", "Lippe"),
                            ("Hals", "Hals"),
                            ("Schulter", "Schulter"),
                            ("Rumpf", "Rumpf"),
                            ("Bauch", "Bauch"),
                            ("Boden", "Boden"),
                            ("Flachboden", "Flachboden"),
                            ("Wackelboden", "Wackelboden"),
                            ("Standfuß", "Standfuß"),
                            ("Standring", "Standring"),
                            ("Knauffuß", "Knauffuß"),
                            ("Ganzes Gefäß", "Ganzes Gefäß"),
                        ],
                        max_length=12,
                        verbose_name="Scherbenform",
                    ),
                ),
                (
                    "vessel_cat",
                    models.CharField(max_length=100, verbose_name="Gefäßkategorie"),
                ),
                (
                    "usage",
                    models.CharField(
                        choices=[
                            ("Kochgeschirr", "Kochgeschirr"),
                            ("Essgeschirr", "Essgeschirr"),
                            ("Trinkgeschirr", "Trinkgeschirr"),
                            ("Feingeschirr", "Feingeschirr"),
                            ("Lagerbehälter", "Lagerbehälter"),
                            ("Transportbehälter", "Transportbehälter"),
                            ("Vorratsgeschirr", "Vorratsgeschirr"),
                            ("Servicegeschirr", "Servicegeschirr"),
                            ("Sonstige Verwendung", "Sonstige Verwendung"),
                            ("Unbekannt", "Unbekannt"),
                        ],
                        max_length=19,
                        verbose_name="Verwendungszweck",
                    ),
                ),
                (
                    "surface",
                    solid_backend.content.fields.ConcatCharField(
                        concat_choices=[
                            (
                                ("unbehandelt", "unbehandelt"),
                                ("geglättet", "geglättet"),
                                ("poliert", "poliert"),
                                ("bemalt", "bemalt"),
                                ("engobiert", "engobiert"),
                                ("glasiert", "glasiert"),
                                ("geschnitten", "geschnitten"),
                                ("geritzt", "geritzt"),
                                ("kammstrichverziert", "kammstrichverziert"),
                                (
                                    "mit Applikation (frei Hand)",
                                    "mit Applikation (frei Hand)",
                                ),
                                (
                                    "mit Applikation (aus der Model)",
                                    "mit Applikation (aus der Model)",
                                ),
                                (
                                    "in Barbotine-Technik verziert",
                                    "in Barbotine-Technik verziert",
                                ),
                                (
                                    "komplexe Merkmalskombination",
                                    "komplexe Merkmalskombination",
                                ),
                            ),
                            (
                                ("unbehandelt", "unbehandelt"),
                                ("geglättet", "geglättet"),
                                ("poliert", "poliert"),
                                ("bemalt", "bemalt"),
                                ("engobiert", "engobiert"),
                                ("glasiert", "glasiert"),
                                ("geschnitten", "geschnitten"),
                                ("geritzt", "geritzt"),
                                ("kammstrichverziert", "kammstrichverziert"),
                                (
                                    "mit Applikation (frei Hand)",
                                    "mit Applikation (frei Hand)",
                                ),
                                (
                                    "mit Applikation (aus der Model)",
                                    "mit Applikation (aus der Model)",
                                ),
                                (
                                    "in Barbotine-Technik verziert",
                                    "in Barbotine-Technik verziert",
                                ),
                                (
                                    "komplexe Merkmalskombination",
                                    "komplexe Merkmalskombination",
                                ),
                            ),
                            (
                                ("unbehandelt", "unbehandelt"),
                                ("geglättet", "geglättet"),
                                ("poliert", "poliert"),
                                ("bemalt", "bemalt"),
                                ("engobiert", "engobiert"),
                                ("glasiert", "glasiert"),
                                ("geschnitten", "geschnitten"),
                                ("geritzt", "geritzt"),
                                ("kammstrichverziert", "kammstrichverziert"),
                                (
                                    "mit Applikation (frei Hand)",
                                    "mit Applikation (frei Hand)",
                                ),
                                (
                                    "mit Applikation (aus der Model)",
                                    "mit Applikation (aus der Model)",
                                ),
                                (
                                    "in Barbotine-Technik verziert",
                                    "in Barbotine-Technik verziert",
                                ),
                                (
                                    "komplexe Merkmalskombination",
                                    "komplexe Merkmalskombination",
                                ),
                            ),
                        ],
                        max_length=400,
                        seperators=[", ", " und "],
                        default="",
                        blank=True,
                        verbose_name="Oberflächenbehandlung",
                    ),
                ),
                (
                    "conserv",
                    models.CharField(
                        choices=[
                            ("Vollständig", "Vollständig"),
                            ("Annähernd vollständig", "Annähernd vollständig"),
                            ("Sehr gut", "Sehr gut"),
                            ("Gut", "Gut"),
                            ("Mäßig", "Mäßig"),
                            ("Stark fragmentiert", "Stark fragmentiert"),
                            ("Schlecht", "Schlecht"),
                        ],
                        max_length=21,
                        verbose_name="Erhaltung",
                    ),
                ),
                ("measures", models.CharField(max_length=200, verbose_name="Maße")),
                (
                    "find",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="formal_aspect",
                        to="ais_content.Find",
                        verbose_name="Fundstück",
                    ),
                ),
            ],
            options={
                "verbose_name": "Formale Aspkete",
                "verbose_name_plural": "Formale Aspkete",
            },
        ),
    ]