from django.urls import path
from .views_backup import (
    MainArticleListCreateView, MainArticleDetailView,
    TrendingNewsListCreateView, TrendingNewsDetailView,
    FeatureNewsListCreateView, FeatureNewsDetailView,
    EventListCreateView, EventDetailView
)

urlpatterns = [
    # Main Article URLs
    path('main-article/', MainArticleListCreateView.as_view(), name='main-article-list-create'),
    path('main-article/<int:pk>/', MainArticleDetailView.as_view(), name='main-article-detail'),

    # Trending News URLs
    path('trending-news/', TrendingNewsListCreateView.as_view(), name='trending-news-list-create'),
    path('trending-news/<int:pk>/', TrendingNewsDetailView.as_view(), name='trending-news-detail'),

    # Feature News URLs
    path('feature-news/', FeatureNewsListCreateView.as_view(), name='feature-news-list-create'),
    path('feature-news/<int:pk>/', FeatureNewsDetailView.as_view(), name='feature-news-detail'),

    # Event URLs
    path('events/', EventListCreateView.as_view(), name='events-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
