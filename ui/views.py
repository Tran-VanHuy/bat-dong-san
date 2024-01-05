from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.
from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse

class HomePage(TemplateView):
	template_name = "home/home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context;

