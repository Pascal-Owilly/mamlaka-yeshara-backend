from django.db import models
from django.contrib.auth.models import User  # Import the User model

class MainArticle(models.Model):
    title = models.CharField(max_length=255)
    # subtitle = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='main_articles/', null=True, blank=True)
    # content = models.TextField()
    # additional_images = models.ImageField(upload_to='main_articles/images/', null=True, blank=True)
    # video = models.FileField(upload_to='videos/', null=True, blank=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_articles', null=True, blank=True)  # Author field

    def __str__(self):
        return f"{self.title} by {self.author}"


class TrendingNews(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='trending_news/', null=True, blank=True)
    content = models.TextField()
    additional_images = models.ImageField(upload_to='trending_news/images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # Update field name and type
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trending_news', null=True, blank=True)  # Author field

    def __str__(self):
        return f"{self.title} by {self.author}"


class FeatureNews(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='feature_news/', null=True, blank=True)
    description = models.TextField()
    additional_images = models.ImageField(upload_to='feature_news/images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # Update field name and type
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feature_news', null=True, blank=True)  # Author field

    def __str__(self):
        return f"{self.title} by {self.author}"


class Event(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    additional_images = models.ImageField(upload_to='events/images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # Update field name and type
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', null=True, blank=True)  # Author field

    def __str__(self):
        return f"{self.title} by {self.author}"
