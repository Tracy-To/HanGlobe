from django.shortcuts import render
from .models import Article
from rest_framework import viewsets, permissions
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  permission_classes = [permissions.AllowAny]