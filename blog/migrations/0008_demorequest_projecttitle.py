# Generated by Django 5.1.1 on 2024-10-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_demorequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="demorequest",
            name="projectTitle",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
