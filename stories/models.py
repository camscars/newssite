from django.db import models
from django.contrib.auth.models import User
from urllib.parse import urlparse

# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=40)
	url = models.URLField()
	points = models.IntegerField(default=1)
	moderator = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	@property
	def domain(self):
		return urlparse(self.url).netloc

	def __str___(self):
		return self.title

	class Meta:
		verbose_name_plural = "Stories" #so that admin site doesnt say "storys"