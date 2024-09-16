from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from rest_framework import generics
from .models import BlogPost, Subscription, ContactUs
from .serializers import BlogPostSerializer, SubscriptionSerializer, ContactUsSerializer
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# REG
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer


class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-id')
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        # Save the blog post instance
        instance = serializer.save()
        # Notify all subscribers about the new blog post
        self.notify_subscribers(instance)

    def notify_subscribers(self, blog_post):
        subscribers = Subscription.objects.all()
        subject = f"New Blog Post: {blog_post.title}"
        html_message = render_to_string('emails/new_blog_post.html', {
            'blog_post': blog_post,
            'current_year': datetime.datetime.now().year
        })
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL

        for subscriber in subscribers:
            to = subscriber.email
            email_message = EmailMultiAlternatives(subject, plain_message, from_email, [to])
            email_message.attach_alternative(html_message, "text/html")
            email_message.send()

class BlogPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        # Save the subscription instance
        instance = serializer.save()
        # Send confirmation email to the user
        self.send_subscription_email(instance.email)

    def send_subscription_email(self, email):
        subject = 'Subscription Confirmation'
        html_message = render_to_string('emails/subscription_email.html', {
            'email': email,
            'current_year': datetime.datetime.now().year
        })
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = email
        email_message = EmailMultiAlternatives(subject, plain_message, from_email, [to])
        email_message.attach_alternative(html_message, "text/html")
        email_message.send()

class SubscriptionListAPIView(generics.ListAPIView):
    queryset = Subscription.objects.all().order_by('-created_at')
    serializer_class = SubscriptionSerializer

class ContactUsCreateAPIView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        # Save the contact message instance
        instance = serializer.save()
        # Send notification email to the admin
        self.send_contact_us_email(instance)

    def send_contact_us_email(self, contact_message):
        subject = 'New Contact Us Message'
        html_message = render_to_string('emails/contact_us_email.html', {
            'name': contact_message.name,
            'email': contact_message.email,
            'message': contact_message.message,
            'current_year': datetime.datetime.now().year
        })
        plain_message = strip_tags(html_message)
        from_email = contact_message.email  # Use the contact message's email as the sender
        to_email = settings.DEFAULT_FROM_EMAIL  # Use the default email from settings as the recipient
        email_message = EmailMultiAlternatives(subject, plain_message, from_email, [to_email])
        email_message.attach_alternative(html_message, "text/html")
        email_message.send()
            
class ContactUsListAPIView(generics.ListAPIView):
    queryset = ContactUs.objects.all().order_by('-created_at')
    serializer_class = ContactUsSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh token not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Invalidate the refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklisting the token
            
            return Response({'detail': 'Logout successful.'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

