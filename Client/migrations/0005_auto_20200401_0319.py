# Generated by Django 3.0.4 on 2020-04-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0004_auto_20200401_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientintake',
            name='entry',
            field=models.TextField(default='ENTRY_DATA'),
        ),
    ]
