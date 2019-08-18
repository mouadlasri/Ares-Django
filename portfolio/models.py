from django.db import models
from tinymce import HTMLField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250,null=True)
    content = HTMLField('Content')
    thumbnail = models.CharField(max_length=120, default=None)
    tech = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.title