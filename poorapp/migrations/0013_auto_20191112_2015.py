# Generated by Django 2.2.6 on 2019-11-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorapp', '0012_auto_20191112_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentprocess',
            name='transaction_num',
            field=models.SlugField(default=313212, max_length=12, unique=True),
            preserve_default=False,
        ),
    ]
