# Generated by Django 4.0 on 2022-05-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plaza', '0017_alter_specialrequest_country_yard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryyard',
            name='yard_num',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]
