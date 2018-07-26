from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class Group(models.Model):
  established = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=50)
  
class Review(models.Model):
  title = models.CharField(max_length=50)
  opinion = models.CharField(max_length=500)
  tag1 = models.CharField(max_length=50)
  tag2 = models.CharField(max_length=50)
  tag3 = models.CharField(max_length=50)
  stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  
class MovieToWatch(models.Model):
  title = models.CharField(max_length=50)
  theater = models.CharField(max_length=100)
  showtime = models.CharField(max_length=8)
  myTime = forms.TimeField(widget=forms.TimeInput(format='%H:%M %p'))
  




