# Generated by Django 3.0.4 on 2020-04-20 09:41

import Client.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Client', '0005_auto_20200417_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='router',
            name='specifications',
        ),
        migrations.AddField(
            model_name='router',
            name='clientDocs',
            field=models.FileField(null=True, upload_to=Client.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='router',
            name='clientDocs1',
            field=models.FileField(null=True, upload_to=Client.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='router',
            name='doc2',
            field=models.FileField(null=True, upload_to=Client.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='router',
            name='doc3',
            field=models.FileField(null=True, upload_to=Client.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='router',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='router', to=settings.AUTH_USER_MODEL),
        ),
    ]
