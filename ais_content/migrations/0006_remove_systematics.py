# Generated by Django 3.0.11 on 2021-02-26 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ais_content", "0005_tree_node_data_migration"),
    ]

    operations = [
        migrations.RemoveField(model_name="find", name="systematics",),
    ]
