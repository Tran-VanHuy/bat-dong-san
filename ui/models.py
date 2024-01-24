from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import User

User._meta.get_field('groups').related_name = 'user_groups'


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

	class Meta:
		verbose_name = "Giới thiệu"
		verbose_name_plural = "Giới thiệu"

	def __str__(self):
		return str(self.title)

class Member(models.Model):
	name = models.CharField(max_length=50)
	avatar = models.FileField(upload_to="static/images", unique=True)

	class Meta:
		verbose_name = "Thành viên"
		verbose_name_plural = "Thành viên"

	def __str__(self):
		return str(self.name)

class Advertisement(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	link = models.TextField()

	class Meta:
		verbose_name = "Quảng cáo"
		verbose_name_plural = "Quảng cáo"

	def __str__(self):
		return mark_safe(f'<img src="{self.image.url}" alt="Image Alt Text" style="width: 200px; height: 100px; object-fit: cover;">')

class Partner(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	link = models.TextField(default="#")

	class Meta:
		verbose_name = "Đối tác"
		verbose_name_plural = "Đối tác"

	def __str__(self):
		return mark_safe(f'<img src="{self.image.url}" style="width: 200px; height: 100px; object-fit: cover;" />')

class Contact(models.Model):
	full_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	email = models.EmailField(max_length=255)
	note = models.TextField()
	read = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Liên hệ"
		verbose_name_plural = "Liên hệ"

	def __str__(self):
		return str(self.note)

class TypeProject(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Kiểu dự án"
		verbose_name_plural = "Kiểu dự án"

	def __str__(self):
		return str(self.name)

class CategoryProject(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Danh mục dự án"
		verbose_name_plural = "Danh mục dự án"

	def __str__(self):
		return str(self.name)
	
class Project(models.Model):
	
	CHOICE_PROJECTS = {
	"0" : "Dự án toàn quốc",
	"1" : "Bất động sản bán lẻ",
	"2" : "Dự án nổi bật"
	}
	image = models.FileField(upload_to="static/images", unique=True)
	type_project = models.ManyToManyField(TypeProject)
	category = models.ManyToManyField(CategoryProject)
	title = models.CharField(max_length=255)
	short_content = models.CharField(max_length=255)
	content = models.TextField()
	price = models.CharField(max_length=100)
	status = models.BooleanField()
	project_sell = models.CharField(
		max_length=2,
		choices=CHOICE_PROJECTS,
		default="0",
		null=True,
		blank=True	
		)

	class Meta:
		verbose_name = "Dự án"
		verbose_name_plural = "Dự án"

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

	class Meta:
		verbose_name = "Trang"
		verbose_name_plural = "Trang"

	def __str__(self):
		return str(self.name)

class Banner(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	page = models.ManyToManyField(Page)

	def __str__(self):
		return mark_safe(f'<img src="{self.image.url}" style="width: 200px; height: 100px; object-fit: cover;" />')

class Sitetour(models.Model):
	CHOICE_SITETOUR = {
	"0": "Nổi bật"
	}
	image = models.FileField(upload_to="static/images", unique=True)
	title = models.CharField(max_length=255)
	short_content = models.CharField(max_length=255)
	content = models.TextField()
	price = models.CharField(max_length=100)
	status = models.BooleanField()
	category_sitetour = models.CharField(
		max_length=1,
		choices=CHOICE_SITETOUR,
		null=True,
		blank=True
		)

	def __str__(self):
		return str(self.title)

class InfoSitetour(models.Model):
	svg = models.TextField()
	name = models.CharField(max_length=100)
	sitetour = models.ForeignKey(Sitetour, on_delete=models.CASCADE, null=True, blank=True, related_name='sitetour_results')

class Advertisement2(models.Model):
	image = models.FileField(upload_to="static/images", unique=True, null=False, blank=False, verbose_name="Ảnh đại diện")
	image1 = models.FileField(upload_to="static/images", unique=True, null=True, blank=True, verbose_name="Ảnh slider 1")
	image2 = models.FileField(upload_to="static/images", unique=True, null=True, blank=True, verbose_name="Ảnh slider 2")
	image3 = models.FileField(upload_to="static/images", unique=True, null=True, blank=True, verbose_name="Ảnh slider 3")
	image4 = models.FileField(upload_to="static/images", unique=True, null=True, blank=True, verbose_name="Ảnh slider 4")
	image5 = models.FileField(upload_to="static/images", unique=True, null=True, blank=True, verbose_name="Ảnh slider 5")
	image6 = models.FileField(upload_to="static/images", unique=True, null=True, blank=True, verbose_name="Ảnh slider 6")
	title = models.CharField(max_length=255, verbose_name="Tiêu đề")
	content = models.TextField(verbose_name="Nội dung")
	price = models.CharField(max_length=50, verbose_name="Giá tiền")
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Tin rao"
		verbose_name_plural = "Tin rao"

	def __str__(self):
		return str(self.title)

class InfoAdvertisement2(models.Model):
	svg = models.TextField()
	name = models.CharField(max_length=100)
	advertisement2 = models.ForeignKey(Advertisement2, on_delete=models.CASCADE, null=True, blank=True, related_name="advertisement_results")

class User(AbstractUser):
	phone = models.CharField(max_length=15, null=True, blank=True)
	class Meta:
		db_table = "users"











	

	





