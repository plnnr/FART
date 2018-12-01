# Generated by Django 2.1.3 on 2018-11-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0004_auto_20181128_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivingsite',
            name='building_size',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receivingsite',
            name='site_far',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sendingsite',
            name='building_size',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sendingsite',
            name='site_far',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]