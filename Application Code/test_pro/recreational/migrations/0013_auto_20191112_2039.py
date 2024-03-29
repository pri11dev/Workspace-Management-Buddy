# Generated by Django 2.2.6 on 2019-11-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recreational', '0012_remove_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(verbose_name='Date of the the Event'),
        ),
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='Name of the Event'),
        ),
        migrations.AlterField(
            model_name='events',
            name='organizer',
            field=models.CharField(max_length=264, verbose_name='Organizer of the the Event'),
        ),
        migrations.AlterField(
            model_name='events',
            name='venue',
            field=models.CharField(max_length=264, verbose_name='Venue of the the Event'),
        ),
    ]
