from django.db import models

# Create your models here.
class Message(models.Model):
  title = models.TextField(null=True, blank=True)
  name = models.TextField(null=True, blank=True)
  email = models.TextField(null=True, blank=True) 
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)