# Generated by Django 2.2.6 on 2019-11-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recreational', '0002_auto_20191109_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=264)),
                ('organizer', models.CharField(max_length=264)),
            ],
        ),
    ]