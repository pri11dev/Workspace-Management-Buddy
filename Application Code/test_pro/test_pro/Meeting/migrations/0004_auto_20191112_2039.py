# Generated by Django 2.2.6 on 2019-11-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0003_auto_20191112_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venture',
            name='desc',
        ),
        migrations.AddField(
            model_name='venture',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='venture',
            name='m1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='venture',
            name='m2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='venture',
            name='m3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='venture',
            name='m4',
            field=models.TextField(default=''),
        ),
    ]
