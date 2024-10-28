from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from django.utils.text import slugify

class BlogPost(models.Model):
    
    SECTION_CHOICES = [
        ('title', 'Title'),
        ('content', 'Content'),
        ('excerpt', 'Excerpt'),
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    sections = models.JSONField(default=list, blank=True)  # Stores section data dynamically
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)

    # Define image and video fields here
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    video = models.FileField(upload_to='blog_videos/', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically generate a unique slug
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            num = 1
            while BlogPost.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def save_sections(self, sections_data):
        """Save sections data to the BlogPost."""
        # Validate sections_data as needed (optional)
        self.sections = sections_data
        self.save()  # Save the instance to persist changes

    def formatted_created_at(self):
        return self.created_at.strftime("%B %d, %Y, %I:%M %p")
        
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to='testimonial_images/', null=True, blank=True)
    client_name = models.CharField(max_length=100)
    client_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

# Request demo

class DemoRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    projectTitle = models.CharField(max_length=255, blank=True, null=True)  # Add this field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Demo Request from {self.name}"
