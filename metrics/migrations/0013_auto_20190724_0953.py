# Generated by Django 2.2.3 on 2019-07-24 04:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0012_auto_20190724_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarprofile',
            name='citations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None),
        ),
    ]
