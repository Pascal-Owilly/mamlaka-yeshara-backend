from rest_framework import generics
from .models_backup import MainArticle, TrendingNews, FeatureNews, Event
from .serializers_backup import MainArticleSerializer, TrendingNewsSerializer, FeatureNewsSerializer, EventSerializer

# Main Article - List and Create
class MainArticleListCreateView(generics.ListCreateAPIView):
    queryset = MainArticle.objects.all().order_by('-id')
    serializer_class = MainArticleSerializer

# Main Article - Retrieve, Update, and Delete
class MainArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainArticle.objects.all().order_by('-id')
    serializer_class = MainArticleSerializer

# Trending News - List and Create
class TrendingNewsListCreateView(generics.ListCreateAPIView):
    queryset = TrendingNews.objects.all().order_by('-id')  # Latest first
    serializer_class = TrendingNewsSerializer

# Trending News - Retrieve, Update, and Delete
class TrendingNewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrendingNews.objects.all()
    serializer_class = TrendingNewsSerializer

# Feature News - List and Create
class FeatureNewsListCreateView(generics.ListCreateAPIView):
    queryset = FeatureNews.objects.all().order_by('-id')  # Latest first
    serializer_class = FeatureNewsSerializer

# Feature News - Retrieve, Update, and Delete
class FeatureNewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeatureNews.objects.all()
    serializer_class = FeatureNewsSerializer

# Event - List and Create
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-id') # Upcoming first
    serializer_class = EventSerializer

# Event - Retrieve, Update, and Delete
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
