# Generated by Django 2.2.6 on 2019-11-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorapp', '0025_auto_20191125_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poorpeople',
            name='identity_number',
            field=models.IntegerField(blank=True, default='123456'),
            preserve_default=False,
        ),
    ]
