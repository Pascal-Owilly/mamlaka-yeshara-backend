###############################################################################################################
# New forms
###############################################################################################################
from django import forms
from .models_backup import MainArticle, TrendingNews, FeatureNews, Event

class MainArticleForm(forms.ModelForm):
    class Meta:
        model = MainArticle
        fields = ['title', 'author',  'image']  # Changed video_url to video
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # 'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'additional_images': forms.FileInput(attrs={'class': 'form-control'}),
            # 'video': forms.FileInput(attrs={'class': 'form-control'}),  # Changed to FileInput
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MainArticleForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['author'].initial = user.username

class TrendingNewsForm(forms.ModelForm):
    class Meta:
        model = TrendingNews
        fields = ['title', 'subtitle', 'author', 'content', 'image', 'additional_images', 'video']  # Changed video_url to video
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'additional_images': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),  # Changed to FileInput
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TrendingNewsForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['author'].initial = user.username

class FeatureNewsForm(forms.ModelForm):
    class Meta:
        model = FeatureNews
        fields = ['title', 'subtitle', 'author', 'description', 'image', 'additional_images', 'video']  # Changed video_url to video
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'additional_images': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),  # Changed to FileInput
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FeatureNewsForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['author'].initial = user.username

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'subtitle', 'author', 'description', 'location', 'image', 'additional_images', 'video', 'date']  # Changed video_url to video
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'additional_images': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),  # Changed to FileInput
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Date widget for better UX
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EventForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['author'].initial = user.username


from django import forms
from .models import Subscription, ContactUs, Testimonial
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['user', 'profile_image', 'client_name', 'client_text']  # Include the new user and profile_image fields


###############################################################################################################
# End New
###############################################################################################################









# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title','sections', 'user'] 

#     # Custom method to handle dynamic sections
#     def save_sections(self, sections_data):
#         blog_post = self.save(commit=False)  # Save the instance without committing to the DB
#         blog_post.sections = sections_data  # Assign the sections data to the instance
#         blog_post.save()  # Now save it to the database
#         return blog_post

