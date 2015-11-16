from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=200)
	# TODO: udelat manualni vyber datumu ...
	date = models.DateTimeField(auto_now_add=True)
	public = models.BooleanField()
	sumary = models.CharField(max_length=1500, null=True, blank=True)
	category = models.ForeignKey(Category)
	text = models.CharField(max_length=20000)
	image1 = models.FileField(upload_to="images/", null=True, blank=True)
	image1_name = models.CharField(max_length=80, null=True, blank=True) 
	image2 = models.FileField(upload_to="images/", null=True, blank=True)
	image2_name = models.CharField(max_length=80, null=True, blank=True)
	image3 = models.FileField(upload_to="images/", null=True, blank=True)
	image3_name = models.CharField(max_length=80, null=True, blank=True)
	image4 = models.FileField(upload_to="images/", null=True, blank=True)
	image4_name = models.CharField(max_length=80, null=True, blank=True)
	image5 = models.FileField(upload_to="images/", null=True, blank=True)
	image5_name = models.CharField(max_length=80, null=True, blank=True) 
	image6 = models.FileField(upload_to="images/", null=True, blank=True)
	image6_name = models.CharField(max_length=80, null=True, blank=True)
	image7 = models.FileField(upload_to="images/", null=True, blank=True)
	image7_name = models.CharField(max_length=80, null=True, blank=True)
	image8 = models.FileField(upload_to="images/", null=True, blank=True)
	image8_name = models.CharField(max_length=80, null=True, blank=True)

	def __unicode__(self):
		return self.title


	
