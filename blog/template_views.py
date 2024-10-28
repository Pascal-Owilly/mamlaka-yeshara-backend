# New Templates
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models_backup import MainArticle, TrendingNews, FeatureNews, Event
from .forms import MainArticleForm, TrendingNewsForm, FeatureNewsForm, EventForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator

###############################################################################################################
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Subscription, ContactUs, Testimonial
from .forms import SubscriptionForm, ContactUsForm, TestimonialForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import datetime
from django.utils import timezone
import json
from django.views.generic import ListView

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'  # Template for listing users
    context_object_name = 'users'  # This variable will be available in the template

    def get_queryset(self):
        return User.objects.all().order_by('-id')  # Fetch all users ordered by ID in descending order

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MainArticleListView(ListView):
    model = MainArticle
    template_name = 'main_article_list.html'
    context_object_name = 'main_articles'

    def get_queryset(self):
        return MainArticle.objects.order_by('-id')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MainArticleDetailView(DetailView):
    model = MainArticle
    template_name = 'main_article_detail.html'
    context_object_name = 'main_article'

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MainArticleCreateView(CreateView):
    model = MainArticle
    form_class = MainArticleForm
    template_name = 'main_article_form.html'
    success_url = reverse_lazy('main_article_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MainArticleUpdateView(UpdateView):
    model = MainArticle
    form_class = MainArticleForm
    template_name = 'main_article_form.html'
    success_url = reverse_lazy('main_article_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MainArticleDeleteView(DeleteView):
    model = MainArticle
    template_name = 'main_article_confirm_delete.html'
    success_url = reverse_lazy('main_article_list')

# Trending News Views
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TrendingNewsListView(ListView):
    model = TrendingNews
    template_name = 'trending_news_list.html'
    context_object_name = 'trending_news'

    def get_queryset(self):
        return TrendingNews.objects.order_by('-id')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TrendingNewsDetailView(DetailView):
    model = TrendingNews
    template_name = 'trending_news_detail.html'
    context_object_name = 'trending_news'

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TrendingNewsCreateView(CreateView):
    model = TrendingNews
    form_class = TrendingNewsForm
    template_name = 'trending_news_form.html'
    success_url = reverse_lazy('trending_news_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TrendingNewsUpdateView(UpdateView):
    model = TrendingNews
    form_class = TrendingNewsForm
    template_name = 'trending_news_form.html'
    success_url = reverse_lazy('trending_news_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TrendingNewsDeleteView(DeleteView):
    model = TrendingNews
    template_name = 'trending_news_confirm_delete.html'
    success_url = reverse_lazy('trending_news_list')

# Feature News Views
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class FeatureNewsListView(ListView):
    model = FeatureNews
    template_name = 'feature_news_list.html'
    context_object_name = 'feature_news'

    def get_queryset(self):
        return FeatureNews.objects.order_by('-id')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class FeatureNewsDetailView(DetailView):
    model = FeatureNews
    template_name = 'feature_news_detail.html'
    context_object_name = 'feature_news'

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class FeatureNewsCreateView(CreateView):
    model = FeatureNews
    form_class = FeatureNewsForm
    template_name = 'feature_news_form.html'
    success_url = reverse_lazy('feature_news_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class FeatureNewsUpdateView(UpdateView):
    model = FeatureNews
    form_class = FeatureNewsForm
    template_name = 'feature_news_form.html'
    success_url = reverse_lazy('feature_news_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class FeatureNewsDeleteView(DeleteView):
    model = FeatureNews
    template_name = 'feature_news_confirm_delete.html'
    success_url = reverse_lazy('feature_news_list')

# Event Views
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.order_by('-id')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event_list')


@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.all().order_by('-created_at')
    return render(request, 'subscription_list.html', {'subscriptions': subscriptions})

@login_required
def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'subscription_list.html', {'form': form})

@login_required
def subscription_edit(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=subscription)
    return render(request, 'subscription_edit.html', {'form': form})

@login_required
def subscription_delete(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription_list')
    return render(request, 'subscription_confirm_delete.html', {'subscription': subscription})

@login_required
def contact_us_list(request):
    messages = ContactUs.objects.all().order_by('-created_at')
    return render(request, 'contact_us_list.html', {'messages': messages})

@login_required
def contact_us_detail(request, pk):
    message = get_object_or_404(ContactUs, pk=pk)
    return render(request, 'contact_us_detail.html', {'message': message})

@login_required
def contact_us_delete(request, pk):
    message = get_object_or_404(ContactUs, pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('contact_us_list')
    return render(request, 'contact_us_delete.html', {'message': message})

@login_required
def testimonial_list(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'testimonial_list.html', {'testimonials': testimonials})

@login_required
def testimonial_create(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'testimonial_form.html', {'form': form})

@login_required
def testimonial_update(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'testimonial_form.html', {'form': form})

@login_required
def testimonial_delete(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonial_list')
    return render(request, 'testimonial_confirm_delete.html', {'testimonial': testimonial})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_post_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('blog_post_list')  # Redirect to blog list after login
    else:
        form = AuthenticationForm()

    # Always return a response object
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page after logout

def notify_subscribers(blog_post):
    # Get all subscribers
    subscribers = Subscription.objects.all()
    subject = f"New Blog Post: {blog_post.title}"

    # Create the email message
    html_message = render_to_string('emails/new_blog_post.html', {
        'blog_post': blog_post,
        'current_year': datetime.datetime.now().year
    })
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL

    # Send email to each subscriber
    for subscriber in subscribers:
        to = subscriber.email
        email_message = EmailMultiAlternatives(subject, plain_message, from_email, [to])
        email_message.attach_alternative(html_message, "text/html")
        email_message.send()


# Feature Article and Article Image Views are similar, just substitute models/forms

# End nwe templates

###############################################################################################################
###############################################################################################################
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from .models import BlogPost, Subscription, ContactUs, Testimonial
# from .forms import BlogPostForm, SubscriptionForm, ContactUsForm, TestimonialForm
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from .forms import SignUpForm, LoginForm
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.conf import settings
# import datetime
# from django.utils import timezone
# import json

# @login_required(login_url='/accounts/login/')  # Redirect to login page if not logged in
# def blog_post_list(request):
#     posts = BlogPost.objects.all().order_by('-created_at')
#     return render(request, 'base.html', {'posts': posts})

# @login_required(login_url='/accounts/login/')
# def blog_post_detail(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     return render(request, 'blog_post_detail.html', {'post': post})

# @login_required(login_url='/accounts/login/')
# def blog_post_create(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         sections = []
#         section_count = int(request.POST.get('total_sections', 0))
        
#         # Collect all sections from the form
#         for i in range(section_count):
#             section_type = request.POST.get(f'section_type_{i}')
#             content = request.POST.get(f'content_{i}')
#             image = request.FILES.get(f'image_{i}')
#             video = request.FILES.get(f'video_{i}')
            
#             # Create a dictionary for each section
#             section = {
#                 'type': section_type,
#                 'content': content,
#             }

#             # Store filenames for images and videos (ensure we are not storing the file object itself)
#             if image:
#                 section['image'] = image.name  # Store only the filename
#             if video:
#                 section['video'] = video.name  # Store only the filename

#             sections.append(section)

#         # Debugging: Print the collected sections
#         print("Collected Sections:", sections)

#         # Create the BlogPost instance
#         blog_post = BlogPost(
#             title=title,
#             sections=sections,  # Store the sections as a JSON-compatible list
#             user=request.user,
#         )
        
#         # Save the blog post to generate an ID before saving files
#         blog_post.save()  
#         notify_subscribers(blog_post)  # Notify subscribers after saving the blog post

#         # Handle file uploads separately
#         for i in range(section_count):
#             section = sections[i]
#             if 'image' in section and request.FILES.get(f'image_{i}'):
#                 image_file = request.FILES.get(f'image_{i}')
#                 # Save the uploaded image
#                 blog_post.image.save(image_file.name, image_file)

#             if 'video' in section and request.FILES.get(f'video_{i}'):
#                 video_file = request.FILES.get(f'video_{i}')
#                 # Save the uploaded video
#                 blog_post.video.save(video_file.name, video_file)

#         # Update the sections again with the filenames or any other processing
#         blog_post.sections = sections
#         blog_post.save()  # Save any changes made to sections

#         return redirect('blog_post_list')

#     return render(request, 'new_blog_post.html')


# @login_required(login_url='/accounts/login/')
# def blog_post_update(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)

#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES, instance=post)

#         if form.is_valid():
#             # Extract section data dynamically after the form has been saved
#             sections_data = []
#             for i in range(int(request.POST.get("total_sections", 0))):
#                 section_type = request.POST.get(f'section_type_{i}')
#                 section_content = request.POST.get(f'content_{i}')  # Ensure this matches your input names

#                 # Handle images and videos separately
#                 image = request.FILES.get(f'image_{i}')
#                 video = request.FILES.get(f'video_{i}')

#                 # Use the actual file if it exists, otherwise use None
#                 sections_data.append({
#                     "type": section_type,
#                     "content": section_content,
#                     "image": image.name if image else None,  # Store filename or None
#                     "video": video.name if video else None    # Store filename or None
#                 })

#             # Now use the custom save method to update sections
#             post = form.save(commit=False)  # Save the form but don't commit yet
#             post.sections = sections_data  # Assign the new sections data
#             post.save()  # Now save the updated BlogPost instance

#             return redirect('blog_post_list')
#     else:
#         form = BlogPostForm(instance=post)

#     return render(request, 'blog_post_form.html', {'form': form, 'sections': post.sections})

    

