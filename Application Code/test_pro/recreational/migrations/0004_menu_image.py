# Generated by Django 2.2.6 on 2019-11-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recreational', '0003_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='img/gallery/05.jpg', upload_to=''),
        ),
    ]
