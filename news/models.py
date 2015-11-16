from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1400)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link1_name = models.CharField(max_length=80, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link2_name = models.CharField(max_length=80, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    link3_name = models.CharField(max_length=80, null=True, blank=True)
    link4 = models.CharField(max_length=200, null=True, blank=True)
    link4_name = models.CharField(max_length=80, null=True, blank=True)
    image1 = models.FileField(upload_to="images/", null=True, blank=True)
    image1_name = models.CharField(max_length=80, null=True, blank=True) 
    image2 = models.FileField(upload_to="images/", null=True, blank=True)
    image2_name = models.CharField(max_length=80, null=True, blank=True)
    image3 = models.FileField(upload_to="images/", null=True, blank=True)
    image3_name = models.CharField(max_length=80, null=True, blank=True)
    image4 = models.FileField(upload_to="images/", null=True, blank=True)
    image4_name = models.CharField(max_length=80, null=True, blank=True)
    

    def __unicode__(self):
        return self.title


class PhotoOfWeek(models.Model):
    title = models.CharField(max_length=80)
    image = models.FileField(upload_to="images/", null=True, blank=True)
    text = models.CharField(max_length=500)
    #date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


