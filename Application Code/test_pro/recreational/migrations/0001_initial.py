# Generated by Django 2.2.6 on 2019-11-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=264)),
                ('Price', models.IntegerField()),
                ('Day', models.CharField(choices=[('SU', 'SUNDAY'), ('MO', 'MONDAY'), ('TU', 'TUESDAY'), ('WE', 'WEDNESDAY'), ('TH', 'THURSDAY'), ('FR', 'FRIDAY'), ('SA', 'SATURDAY')], max_length=2)),
            ],
        ),
    ]
