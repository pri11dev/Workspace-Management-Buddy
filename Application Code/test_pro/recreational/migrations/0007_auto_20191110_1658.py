# Generated by Django 2.2.6 on 2019-11-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recreational', '0006_auto_20191110_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
