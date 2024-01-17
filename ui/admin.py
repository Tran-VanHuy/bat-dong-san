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

admin.site.register(Introduce)
admin.site.register(Member)
admin.site.register(Advertisement)
admin.site.register(Partner)
admin.site.register(Contact)
admin.site.register(Project,ProjectAdmin)
admin.site.register(TypeProject)
admin.site.register(CategoryProject)








