# Generated by Django 5.0.6 on 2024-07-14 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymap', '0003_rename_lat_ministry_latitude_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ministry',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='ministry',
            old_name='longitude',
            new_name='lng',
        ),
    ]
