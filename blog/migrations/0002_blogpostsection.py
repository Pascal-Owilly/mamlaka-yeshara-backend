# Generated by Django 5.1.1 on 2024-10-25 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('excerpt', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_sections/')),
                ('video', models.FileField(blank=True, null=True, upload_to='blog_sections/')),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='blog.blogpost')),
            ],
        ),
    ]