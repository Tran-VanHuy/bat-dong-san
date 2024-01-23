from django.contrib import admin
from .models import *
from django.db import models
from django.forms import CheckboxSelectMultiple
from django import forms


# Register your models here.
class InfoProjectInline(admin.StackedInline):
    model = InfoProject
    extra = 1
    formfield_overrides = {
    	models.ManyToManyField : {'widget': CheckboxSelectMultiple}
    }
  	

class ProjectAdmin(admin.ModelAdmin):
   	inlines = [InfoProjectInline]

# review
class InfoReviewInline(admin.StackedInline):
    model = InfoReview
    extra = 1
    formfield_overrides = {
        models.ManyToManyField : {'widget': CheckboxSelectMultiple}
    }
    

class ReviewAdmin(admin.ModelAdmin):
    inlines = [InfoReviewInline]

# Sitetour
class InfoSitetourInline(admin.StackedInline):
    model = InfoSitetour
    extra = 1
    

class SitetourAdmin(admin.ModelAdmin):
    inlines = [InfoSitetourInline]

# 

class Advertisement2Inline(admin.StackedInline):
    model = InfoAdvertisement2

class Advertisement2Admin(admin.ModelAdmin):
    inlines = [Advertisement2Inline]

admin.site.register(Introduce)
admin.site.register(Member)
admin.site.register(Advertisement)
admin.site.register(Partner)
admin.site.register(Contact)
admin.site.register(Project,ProjectAdmin)
# admin.site.register(TypeProject)
# admin.site.register(CategoryProject)
admin.site.register(Page)
admin.site.register(Banner)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Sitetour, SitetourAdmin)
admin.site.register(Advertisement2, Advertisement2Admin)













