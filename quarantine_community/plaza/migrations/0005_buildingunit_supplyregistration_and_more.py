# Generated by Django 4.0 on 2022-05-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plaza', '0004_specialrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SupplyRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.CharField(max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='countryyard',
            name='name',
        ),
        migrations.AddField(
            model_name='countryyard',
            name='yard_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]