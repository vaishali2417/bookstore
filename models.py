
from django.db import models
from django.urls import reverse
from django.templatetags.static import static

class Book(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)
    imagename = models.CharField(max_length = 2083, default=False)
    category = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @property
    def img_url(self):
        return static("icons/{}".format(self.imagename))


class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title
