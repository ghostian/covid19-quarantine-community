# Generated by Django 4.0 on 2022-05-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidbasicinfo',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
