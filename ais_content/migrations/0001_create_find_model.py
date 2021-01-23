# Generated by Django 3.0.11 on 2021-01-23 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_create_tree_node_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Find',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('storage', models.CharField(max_length=300, null=True, blank=True, verbose_name='Stadt, Museum/ Sammlung')),
                ('find_number', models.CharField(max_length=200, null=True, blank=True, verbose_name='Fundnummer')),
                ('inven_number', models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='Inventarnummer')),
                ('source', models.CharField(max_length=300, null=True, verbose_name='Publikation')),
                ('description', models.TextField(max_length=400, null=True, blank=True, verbose_name='Beschreibung')),
                ('systematics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profiles', to='content.TreeNode', verbose_name='Steckbrief-Ebene')),
            ],
            options={
                'verbose_name': 'Fundstück',
                'verbose_name_plural': 'Fundstücke',
            },
        ),
    ]
