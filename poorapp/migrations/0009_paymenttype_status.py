# Generated by Django 2.2.6 on 2019-11-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorapp', '0008_auto_20191112_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttype',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
