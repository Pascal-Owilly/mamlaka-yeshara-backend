###############################################################################################################
# New urls
###############################################################################################################
from django.urls import path
from . import template_views

urlpatterns = [
    path('users/', template_views.UserListView.as_view(), name='user_list'),  # URL for the user list view

    path('main-articles/', template_views.MainArticleListView.as_view(), name='main_article_list'),
    path('main-articles/<int:pk>/', template_views.MainArticleDetailView.as_view(), name='main_article_detail'),
    path('main-articles/add/', template_views.MainArticleCreateView.as_view(), name='main_article_create'),
    path('main-articles/edit/<int:pk>/', template_views.MainArticleUpdateView.as_view(), name='main_article_update'),
    path('main-articles/delete/<int:pk>/', template_views.MainArticleDeleteView.as_view(), name='main_article_delete'),

    path('trending-news/', template_views.TrendingNewsListView.as_view(), name='trending_news_list'),
    path('trending-news/<int:pk>/', template_views.TrendingNewsDetailView.as_view(), name='trending_news_detail'),
    path('trending-news/add/', template_views.TrendingNewsCreateView.as_view(), name='trending_news_create'),
    path('trending-news/edit/<int:pk>/', template_views.TrendingNewsUpdateView.as_view(), name='trending_news_update'),
    path('trending-news/delete/<int:pk>/', template_views.TrendingNewsDeleteView.as_view(), name='trending_news_delete'),

    path('', template_views.FeatureNewsListView.as_view(), name='feature_news_list'),
    path('feature-news/<int:pk>/', template_views.FeatureNewsDetailView.as_view(), name='feature_news_detail'),
    path('feature-news/add/', template_views.FeatureNewsCreateView.as_view(), name='feature_news_create'),
    path('feature-news/edit/<int:pk>/', template_views.FeatureNewsUpdateView.as_view(), name='feature_news_update'),
    path('feature-news/delete/<int:pk>/', template_views.FeatureNewsDeleteView.as_view(), name='feature_news_delete'),

    path('events/', template_views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', template_views.EventDetailView.as_view(), name='event_detail'),
    path('events/add/', template_views.EventCreateView.as_view(), name='event_create'),
    path('events/edit/<int:pk>/', template_views.EventUpdateView.as_view(), name='event_update'),
    path('events/delete/<int:pk>/', template_views.EventDeleteView.as_view(), name='event_delete'),

    # more
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



###############################################################################################################
# end New 
###############################################################################################################



# from django.urls import path


# urlpatterns = [
#     path('', template_views.blog_post_list, name='blog_post_list'),
#     path('blog-posts/<int:pk>/', template_views.blog_post_detail, name='blog_post_detail'),
#     path('blog-posts/new/', template_views.blog_post_create, name='blog_post_create'),
#     path('blog-posts/<int:pk>/edit/', template_views.blog_post_update, name='blog_post_update'),
#     path('blog-posts/<int:pk>/delete/', template_views.blog_post_delete, name='blog_post_delete'),

