from django.db import models
from django.db.models.fields import CharField
from django.utils.timezone import now


# Create your models here.

class BoardModel(models.Model):
  board_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100, blank=False)
  content = models.TextField(blank=False)
  author = models.CharField(max_length=20, blank=False)
  file = models.FileField(blank=True, upload_to='')
  good = models.IntegerField(blank=True, default=0)
  read = models.IntegerField(blank=True, default=0)
  delete_flg = models.BooleanField(default=False)
  delete_date = models.DateTimeField(blank=True, null=True)
  create_date = models.DateTimeField(default=now, blank=True)
