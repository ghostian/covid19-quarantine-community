# Generated by Django 4.0 on 2022-05-28 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0002_covidbasicinfo_expected_end_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
