# Generated by Django 2.1.3 on 2018-12-04 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0010_auto_20181204_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='receiving_site',
        ),
    ]