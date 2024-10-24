from django.urls import path
from . import template_views

urlpatterns = [
    path('', template_views.blog_post_list, name='blog_post_list'),
    path('blog-posts/<int:pk>/', template_views.blog_post_detail, name='blog_post_detail'),
    path('blog-posts/new/', template_views.blog_post_create, name='blog_post_create'),
    path('blog-posts/<int:pk>/edit/', template_views.blog_post_update, name='blog_post_update'),
    path('blog-posts/<int:pk>/delete/', template_views.blog_post_delete, name='blog_post_delete'),
    path('subscriptions/', template_views.subscription_list, name='subscription_list'),
    path('subscriptions/new/', template_views.subscription_create, name='subscription_create'),
    path('subscriptions/<int:pk>/edit/', template_views.subscription_edit, name='subscription_edit'),
    path('subscriptions/<int:pk>/delete/', template_views.subscription_delete, name='subscription_delete'),
    path('contact-us/', template_views.contact_us_list, name='contact_us_list'),
     path('contact-us/<int:pk>/', template_views.contact_us_detail, name='contact_us_detail'),
    path('contact-us/<int:pk>/delete/', template_views.contact_us_delete, name='contact_us_delete'),
    path('testimonials-list/', template_views.testimonial_list, name='testimonial_list'),
    path('testimonials-create/new/', template_views.testimonial_create, name='add_testimonial'),
    path('testimonials-edit/<int:pk>/edit/', template_views.testimonial_update, name='testimonial_update'),
    path('testimonials-delete/<int:pk>/delete/', template_views.testimonial_delete, name='testimonial_delete'),

    # Authentication URLs
    path('signup/', template_views.signup_view, name='signup'),
    path('login/', template_views.login_view, name='login'),
    path('logout/', template_views.logout_view, name='logout'),
]
