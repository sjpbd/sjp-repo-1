# Generated by Django 5.0.6 on 2024-07-12 04:03

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0002_ministrytype_alter_ministry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministry',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
