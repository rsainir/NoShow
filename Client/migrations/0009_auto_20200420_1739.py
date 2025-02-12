# Generated by Django 3.0.4 on 2020-04-20 17:39

import Client.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0008_auto_20200420_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='clientDocs',
            field=models.FileField(null=True, upload_to=Client.models.user_directory_path, verbose_name='Letter of Engagement (Word.docx)'),
        ),
        migrations.AlterField(
            model_name='router',
            name='clientDocs1',
            field=models.FileField(null=True, upload_to=Client.models.user_directory_path, verbose_name='Letter of Engagement (PDF)'),
        ),
    ]
