# Generated by Django 4.0 on 2022-06-03 14:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plaza', '0023_alter_buildingsubunit_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BentoBoxRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.CharField(max_length=16)),
                ('requested_num', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('resolved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('building_subunit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bs_bento', to='plaza.buildingsubunit')),
                ('building_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bu_bento', to='plaza.buildingunit')),
                ('country_yard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cy_bento', to='plaza.countryyard')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
