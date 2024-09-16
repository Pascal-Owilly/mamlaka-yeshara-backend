from django.contrib import admin
from .models import BlogPost, Subscription, ContactUs

# Register each model individually
admin.site.register(BlogPost)
admin.site.register(Subscription)
admin.site.register(ContactUs)
