# Generated by Django 2.2.6 on 2020-01-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorapp', '0031_remove_blooddoner_bdoner_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddoner',
            name='bdoner_gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]
