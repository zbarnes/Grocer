from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class DemoView(TemplateView):
    template_name = "testapp/test.html"