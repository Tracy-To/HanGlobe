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

  title = models.CharField(max_length=200, blank=False)
  content = models.TextField(blank=False)
  media = models.URLField(blank=True, null=True)
  category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=False)
  author = models.CharField(max_length=100, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  
  def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y')
  
  def formatted_updated_date(self):
        return self.updated_at.strftime('%B %d, %Y')
