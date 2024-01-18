"""
URL configuration for realestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ui.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path("danh-sach-du-an", ListProjectPage.as_view(), name="list-projects"),
    path("danh-sach-tin-rao", AdvertisementPage.as_view(), name="advertisement"),
    path("chi-tiet-tin-rao/<slug>", AdvertisementDetailPage.as_view(), name="advertisement-detail"),
    path("danh-sach-tin-tuc", NewsPage.as_view(), name="news"),
    path("chi-tiet-tin-tuc/<slug>", NewsDetailPage.as_view(), name="news-detail"),
    path("danh-sach-sitetour", SitetourPage.as_view(), name="sitetour"),
    path("chi-tiet-sitetour/<slug>", SitetourDetailPage.as_view(), name="sitetour-detail"),
    
]
