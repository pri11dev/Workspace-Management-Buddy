# Generated by Django 2.2.6 on 2019-11-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recreational', '0007_auto_20191110_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.CharField(max_length=20),
        ),
    ]