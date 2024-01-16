from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.
from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse
from .models import *

class HomePage(TemplateView):
	template_name = "home/home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['introduces'] = Introduce.objects.filter(question_type='0')
		context['strengths'] =  Introduce.objects.filter(question_type='1')
		context['members'] = Member.objects.all()
		context['advertisements'] = Advertisement.objects.all()
		return context;

class ListProjectPage(TemplateView):
	template_name = "projects/list-projects.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context;

class AdvertisementPage(TemplateView):
	template_name = "advertisement/advertisement.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class AdvertisementDetailPage(TemplateView):
	template_name = "advertisement/advertisement-detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class NewsPage(TemplateView):
	template_name = "news/news.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class NewsDetailPage(TemplateView):
	template_name = "news/news-detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class SitetourPage(TemplateView):
	template_name = "sitetour/sitetour.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class SitetourDetailPage(TemplateView):
	template_name = "sitetour/sitetour-detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
		

