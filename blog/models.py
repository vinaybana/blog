from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
	title= models.CharField(max_length=200)
	text=models.TextField()
	slug=models.SlugField(max_length=70)
	parent=models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
	created_date = models.DateTimeField(default = timezone.now)

	class Meta:
		verbose_name_plural = "categories" 

	def __str__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(blank=True, max_length=200)
	text=models.TextField(default=True)
	slug=models.SlugField(max_length=70, blank=True)
	created_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title


class Post(models.Model):
	tag = models.ManyToManyField('Tag')
	category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_query_name="posts")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	slug = models.SlugField(blank=True)
	

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title 
		
	




			
	
	
