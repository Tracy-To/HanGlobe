from .models import Article
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'media', 'category', 'author']
