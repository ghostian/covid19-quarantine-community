# Generated by Django 4.0 on 2022-05-30 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plaza', '0013_alter_specialrequest_building_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplyregistration',
            name='building_subunit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bs', to='plaza.buildingsubunit'),
            preserve_default=False,
        ),
    ]
