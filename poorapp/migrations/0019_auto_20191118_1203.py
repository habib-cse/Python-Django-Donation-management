# Generated by Django 2.2.6 on 2019-11-18 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poorapp', '0018_auto_20191118_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doner',
            name='district_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorapp.DistrictList'),
        ),
        migrations.AlterField(
            model_name='poorpeople',
            name='district_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorapp.DistrictList'),
        ),
    ]
