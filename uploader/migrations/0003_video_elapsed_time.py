# Generated by Django 3.2.15 on 2022-09-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20220915_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='elapsed_time',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
