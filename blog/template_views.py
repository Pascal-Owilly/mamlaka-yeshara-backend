from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Subscription, ContactUs, Testimonial
from .forms import BlogPostForm, SubscriptionForm, ContactUsForm, TestimonialForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import datetime

@login_required(login_url='/accounts/login/')  # Redirect to login page if not logged in
def blog_post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'base.html', {'posts': posts})

@login_required(login_url='/accounts/login/')
def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'post': post})

@login_required(login_url='/accounts/login/')
def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            notify_subscribers(blog_post)
            return redirect('blog_post_list')
    else:
        form = BlogPostForm()
    return render(request, 'new_blog_post.html', {'form': form})

@login_required(login_url='/accounts/login/')
def blog_post_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_post_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def blog_post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_post_list')
    return render(request, 'blog_post_confirm_delete.html', {'post': post})


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
