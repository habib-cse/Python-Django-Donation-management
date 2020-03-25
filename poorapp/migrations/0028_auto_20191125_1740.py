# Generated by Django 2.2.6 on 2019-11-25 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poorapp', '0027_auto_20191125_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poorpeople',
            old_name='identity_number',
            new_name='identity_doc_number',
        ),
        migrations.RenameField(
            model_name='poorpeople',
            old_name='payment_account',
            new_name='payment_type_account',
        ),
        migrations.AddField(
            model_name='doner',
            name='doner_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doner',
            name='doner_gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='poorpeople',
            name='aplicant_age',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='poorpeople',
            name='aplicant_gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='poorpeople',
            name='identity_doc_type',
            field=models.CharField(choices=[('DL', 'Driving License'), ('PP', 'Passport'), ('NC', 'Nid Card'), ('BC', 'Birth Certificate')], max_length=2),
        ),
        migrations.CreateModel(
            name='BloodDoner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bdoner_name', models.CharField(max_length=200)),
                ('last_donate_date', models.DateField()),
                ('bdoner_phone', models.CharField(max_length=20)),
                ('bdoner_gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1, null=True)),
                ('bdoner_age', models.IntegerField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('bdoner_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorapp.CityList')),
                ('bdoner_district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorapp.DistrictList')),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorapp.BlodGroup')),
            ],
        ),
    ]
