# Generated by Django 2.0.4 on 2018-05-11 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20180420_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deskrisaun',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]