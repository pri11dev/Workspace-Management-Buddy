# Generated by Django 2.2.6 on 2019-11-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recreational', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Day',
            field=models.IntegerField(choices=[(6, 'SUNDAY'), (0, 'MONDAY'), (1, 'TUESDAY'), (2, 'WEDNESDAY'), (3, 'THURSDAY'), (4, 'FRIDAY'), (5, 'SATURDAY')]),
        ),
    ]
