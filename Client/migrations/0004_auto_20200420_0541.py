# Generated by Django 3.0.4 on 2020-04-20 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_auto_20200420_0447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientintake',
            old_name='progress',
            new_name='progress_C',
        ),
        migrations.AddField(
            model_name='clientintake',
            name='progress_A',
            field=models.CharField(choices=[('1', 'Client Intake & Engagement Letter Sent'), ('2', 'Initial TM or Copyright Search'), ('3', 'Trademark Clearance Letter & Client Update'), ('4', 'Initial Filing'), ('5', 'USPTO Response Filing'), ('6', 'Publication for Opposition'), ('7', 'Filing Accepted and Completed with the USPTO')], default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='clientintake',
            name='progress_B',
            field=models.CharField(choices=[('1', 'Client Intake & Engagement Letter Sent'), ('2', 'Initial Draft Prepared'), ('3', 'Reviewed by Client'), ('4', 'Final Draft Sent')], default=1, max_length=100),
        ),
    ]