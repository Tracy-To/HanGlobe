from django.db import models

class Article(models.Model):
  CATEGORY_CHOICES = [
    ('sights_landmarks', 'Sights & Landmarks'),
    ('cities_towns', 'Cities & Towns'),
    ('food_dining', 'Food & Dining'),
    ('cafes', 'Cafés'),
    ('activities_leisure', 'Activities & Leisure'),
    ('daily_life', 'Daily Life Essentials'),
    ('travel_tips', 'Travel Tips'),
  ]

  title = models.CharField(max_length=200)
  content = models.TextField()
  media = models.URLField(blank=True, null=True)
  category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
  author = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  