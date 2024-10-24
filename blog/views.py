from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from rest_framework import generics
from .models import BlogPost, Subscription, ContactUs, Testimonial
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

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError



class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-id')
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
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

    def create(self, request, *args, **kwargs):
        # Check if a subscription with the provided email already exists
        email = request.data.get('email')
        if Subscription.objects.filter(email=email).exists():
            return Response(
                {"status": "error", "message": "This email is already subscribed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            # If the email does not exist, create a new subscription
            super().create(request, *args, **kwargs)
            return Response(
                {"status": "success", "message": "Thank you for subscribing!"},
                status=status.HTTP_201_CREATED
            )
        except ValidationError:
            # Handle validation errors explicitly
            return Response(
                {"status": "error", "message": "There was an error with your subscription. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )

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

    def create(self, request, *args, **kwargs):
        try:
            # Attempt to create the contact message
            super().create(request, *args, **kwargs)
            return Response(
                {"status": "success", "message": "Your message has been sent successfully."},
                status=status.HTTP_201_CREATED
            )
        except ValidationError:
            # Handle validation errors explicitly
            return Response(
                {"status": "error", "message": "There was an error sending your message. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )

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

from .serializers import TestimonialSerializer

class TestimonialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all().order_by('-created_at')
    serializer_class = TestimonialSerializer

class TestimonialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

# views.py
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.decorators import api_view
from .models import DemoRequest
from .serializers import DemoRequestSerializer

@csrf_exempt
@api_view(['POST'])
def request_demo(request):
    serializer = DemoRequestSerializer(data=request.data)

    if serializer.is_valid():
        demo_request = serializer.save()  # Save the demo request

        # Send email notification
        try:
            send_mail(
                f'New Demo Request for {demo_request.projectTitle}',  # Use project title here
                f"A new demo request has been received from {demo_request.name}.\n\n"
                f"Email: {demo_request.email}\n"
                f"Project Title: {demo_request.projectTitle}\n"  # Include project title in the email
                f"Message: {demo_request.message}",
                settings.DEFAULT_FROM_EMAIL,
                ['owillypascal@gmail.com', 'mariallugare@gmail.com', 'intellima.tech@gmail.com', 'pasclouma54@gmal.com'],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Demo request sent successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Failed to send demo request.', 'error': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid data.', 'errors': serializer.errors}, status=400)

