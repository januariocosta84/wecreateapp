# Generated by Django 2.0.4 on 2018-04-20 06:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20180420_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran', models.CharField(max_length=40)),
                ('titulo', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=43)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_requijisaun', models.DateTimeField(auto_now=True)),
                ('data_entrega', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='fornesedor',
            name='Nasaun',
            field=models.CharField(choices=[('TL', 'Timor Leste'), ('IN', 'Indonesia')], default='Timor Leste', max_length=30),
        ),
    ]