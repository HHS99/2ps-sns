from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class BoardModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=50)
  snsImage = models.ImageField(upload_to='')
  good = models.IntegerField()
  read = models.IntegerField()
  readText = models.TextField()
