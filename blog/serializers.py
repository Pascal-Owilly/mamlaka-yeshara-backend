from rest_framework import serializers
from .models import BlogPost, ContactUs, Subscription
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class BlogPostSerializer(serializers.ModelSerializer):
    sections_by_type = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'image', 'video', 'created_at', 'user', 'sections_by_type']

    def get_sections_by_type(self, obj):
        sections_by_type = {choice[0]: [] for choice in BlogPost.SECTION_CHOICES}
        for section in obj.sections:
            section_type = section.get("type")
            if section_type in sections_by_type:
                sections_by_type[section_type].append(section)
        return sections_by_type


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

# REG
# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'user', 'profile_image', 'client_name', 'client_text', 'created_at']


from .models import DemoRequest

class DemoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoRequest
        fields = ['name', 'email', 'message', 'projectTitle']  # Include projectTitle

