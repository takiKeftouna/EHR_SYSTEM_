# Generated by Django 4.0.4 on 2022-05-11 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patien',
            name='phone',
            field=models.IntegerField(default=False),
        ),
    ]