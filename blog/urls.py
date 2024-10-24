from django.urls import path
from .views import (
    BlogPostListCreateAPIView, BlogPostDetailAPIView,
    SubscriptionListAPIView, SubscriptionCreateAPIView,
    ContactUsListAPIView, ContactUsCreateAPIView,
    UserRegistrationView, LogoutView,
    TestimonialListCreateAPIView, TestimonialDetailAPIView, request_demo
)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    # BlogPost URLs
    path('blogposts/', BlogPostListCreateAPIView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostDetailAPIView.as_view(), name='blogpost-detail'),

    # Subscription URLs
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscription-list'),
    path('subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),

    # ContactUs URLs
    path('contact-us/', ContactUsListAPIView.as_view(), name='contact-us-list'),
    path('contact-us/create/', ContactUsCreateAPIView.as_view(), name='contact-us-create'),

    # Testimonials
    path('testimonials/', TestimonialListCreateAPIView.as_view(), name='testimonial-list-create'),
    path('testimonials/<int:pk>/', TestimonialDetailAPIView.as_view(), name='testimonial-detail'),

    # Request demo
    path('request-demo/', request_demo, name='request-demo'),

    # User Registration
    # path('register/', UserRegistrationView.as_view(), name='register'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Logout
    # path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
