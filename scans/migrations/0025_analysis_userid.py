# Generated by Django 4.1.4 on 2023-01-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0024_remove_analysis_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='userid',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]