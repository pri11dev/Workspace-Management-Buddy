# Generated by Django 2.2.6 on 2019-11-12 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recreational', '0011_auto_20191110_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
    ]
