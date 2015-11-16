from django.db import models

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80, null=True, blank=True)
    mail = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    text = models.CharField(max_length=1400)
    
    def __unicode__(self):
        return self.title


