from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class Partner(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	link = models.TextField(default="#")

	def __str__(self):
		return mark_safe(f'<img src="{self.image.url}" style="width: 200px; height: 100px; object-fit: cover;" />')

class Contact(models.Model):
	full_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	email = models.EmailField(max_length=255)
	note = models.TextField()
	read = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.note)

class TypeProject(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return str(self.name)

class CategoryProject(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return str(self.name)
	
class Project(models.Model):
	
	image = models.FileField(upload_to="static/images", unique=True)
	type_project = models.ManyToManyField(TypeProject)
	category = models.ManyToManyField(CategoryProject)
	title = models.CharField(max_length=255)
	short_content = models.CharField(max_length=255)
	content = models.TextField()
	price = models.CharField(max_length=100)
	status = models.BooleanField()

	def __str__(self):
		return str(self.title)

class Review(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	video = models.FileField(upload_to="static/images", unique=True)
	title = models.CharField(max_length=255)
	status = models.BooleanField()

	def __str__(self):
		return str(self.title)

class InfoReview(models.Model):
	svg = models.TextField()
	name = models.CharField(max_length=100)
	review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True, related_name='review_results')

class InfoProject(models.Model):
	svg = models.TextField()
	name = models.CharField(max_length=100)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='project_results')

class Page(models.Model):
	name = models.CharField(max_length=50, unique=True)
	link = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.name)

class Banner(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	page = models.ManyToManyField(Page)

	def __str__(self):
		return mark_safe(f'<img src="{self.image.url}" style="width: 200px; height: 100px; object-fit: cover;" />')

class Sitetour(models.Model):
	image = models.FileField(upload_to="static/images")
	title = models.CharField(max_length=255)
	short_content = models.CharField(max_length=255)
	content = models.TextField()
	price = models.CharField(max_length=100)
	status = models.BooleanField()

	def __str__(self):
		return str(self.title)

class InfoSitetour(models.Model):
	svg = models.TextField()
	name = models.CharField(max_length=100)
	sitetour = models.ForeignKey(Sitetour, on_delete=models.CASCADE, null=True, blank=True, related_name='sitetour_results')









	

	





