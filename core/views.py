from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
  template_name = "home.html"

class MessageCreateView(CreateView):
  model = Message
  template_name = "message/message_form.html"
  fields = ('status', 'name', 'email', 'message')
  success_url = reverse_lazy('success')

class Success(TemplateView):
  template_name = "success.html"

class AboutMe(TemplateView):
  template_name = "about_me.html"

class Resume(TemplateView):
  template_name = "resume.html"