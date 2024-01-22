from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.
from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse
from . import forms
import json
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import F, OuterRef, Prefetch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class HomePage(TemplateView):
	template_name = "home/home.html"
	form_class = forms.ContactForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['introduces'] = Introduce.objects.filter(question_type='0')
		context['strengths'] =  Introduce.objects.filter(question_type='1')
		context['members'] = Member.objects.all()
		context['advertisements'] = Advertisement.objects.all()
		context['partners'] = Partner.objects.all()
		context['form'] = self.form_class()
		context['project_main'] = Project.objects.prefetch_related(
		Prefetch(
			'project_results',
			queryset=(
				InfoProject.objects.all()
				)
			)
		).filter(status=True).order_by("id").first()
		context['project_outstanding'] = Project.objects.prefetch_related(
		Prefetch(
			'project_results',
			queryset=(
				InfoProject.objects.filter()
				)
			)
		).exclude(id=context['project_main'].id).filter(status=True).order_by("-id")
		context['banners'] = Banner.objects.filter(page__name__iexact="trang chủ")
		context['reviews'] = Review.objects.prefetch_related(
			Prefetch('review_results', queryset=InfoReview.objects.all())
			).filter(status=True)
		context['sitetours'] = Sitetour.objects.prefetch_related(Prefetch('sitetour_results', queryset=InfoSitetour.objects.all())).filter(status=True)
		context['sell_projects'] = Project.objects.prefetch_related(Prefetch('project_results', queryset=InfoProject.objects.all())).filter(project_sell="1", status=True)[0:4]
		return context


	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = self.form_class(self.request.POST)

		if form.is_valid():
			form.save()
			context['message_contact'] = "Gửi thành công"

		return self.render_to_response(context)

class ListProjectPage(TemplateView):
	template_name = "projects/list-projects.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		projects = Project.objects.prefetch_related(Prefetch("project_results", queryset=InfoProject.objects.all())).filter(status=True, project_sell="0")
		context['project_main'] = Project.objects.prefetch_related(
			Prefetch(
				'project_results',
				queryset=(
					InfoProject.objects.all()
					)
				)
		).filter(status=True, project_sell="2").order_by("-id")
		
		context['count_projects'] = Project.objects.filter(status=True, project_sell="0").count()
		paginator = Paginator(projects, 8)
		page = self.request.GET.get('page', 1)
		projects = paginator.page(page)
		
		
		
		context['reviews'] = Review.objects.prefetch_related(
			Prefetch('review_results', queryset=InfoReview.objects.all())
			).filter(status=True)
		context['sitetours'] = Sitetour.objects.prefetch_related(Prefetch('sitetour_results', queryset=InfoSitetour.objects.all())).filter(status=True).first()
		context['projects'] = projects
		return context

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

		context['sitetour_outstanding'] = Sitetour.objects.prefetch_related(Prefetch('sitetour_results', queryset=InfoSitetour.objects.all())).filter(category_sitetour="0", status=True)
		sitetours = Sitetour.objects.prefetch_related(Prefetch('sitetour_results', queryset=InfoSitetour.objects.all())).exclude(category_sitetour="0", status=False)
		
		paginator = Paginator(sitetours, 6)
		page = self.request.GET.get('page', 1)
		sitetours = paginator.page(page)

		context['sitetours'] = sitetours
		return context

class SitetourDetailPage(TemplateView):
	template_name = "sitetour/sitetour-detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
		

