# Generated by Django 3.2.10 on 2024-09-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeshara', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image_url',
        ),
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='properties/'),
        ),
    ]
