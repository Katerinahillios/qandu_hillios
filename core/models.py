from django.db import models
title_options = (
(0, 'Select...'),
(1, 'Mr'),
(2, 'Ms'),
(3, 'Mrs'),
(4, 'Dr'),
)

# Create your models here.
class Message(models.Model):
  status = models.IntegerField(choices=title_options, default=0)
  name = models.CharField(max_length=300, default="")
  email = models.CharField(max_length=300, default="")
  message = models.TextField(null=True, blank=True, default="")
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
     return self.name