# blog/serializers.py

from rest_framework import serializers
from .models_backup import MainArticle, TrendingNews, FeatureNews, Event

class MainArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainArticle
        fields = '__all__'

class TrendingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingNews
        fields = '__all__'

class FeatureNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureNews
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
