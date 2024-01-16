from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Introduce(models.Model):
	svg = models.TextField()
	title = models.CharField(max_length=255)
	short_content = models.CharField(max_length=150)
	content = models.CharField(max_length=255)
	question_type = models.CharField(
		max_length=1,
		null=True,
		choices=[
			('0', 'introduce'),
			('1', 'strengths')
		]
	)

	def __str__(self):
		return str(self.title)

class Member(models.Model):
	name = models.CharField(max_length=50)
	avatar = models.FileField(upload_to="static/images", unique=True)

	def __str__(self):
		return str(self.name)

class Advertisement(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	link = models.TextField()

	def __str__(self):
		return mark_safe(f'<img src="{self.image.url}" alt="Image Alt Text" style="width: 200px; height: 100px; object-fit: cover;">')

