from django.contrib import admin
from .models import BlogPost, Subscription, ContactUs, Testimonial

# Register each model individually
admin.site.register(BlogPost)
admin.site.register(Subscription)
admin.site.register(ContactUs)
admin.site.register(Testimonial)



from django.contrib import admin
from .models_backup import MainArticle, TrendingNews, FeatureNews, Event

admin.site.register(MainArticle)
admin.site.register(TrendingNews)
admin.site.register(FeatureNews)
admin.site.register(Event)
