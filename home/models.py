
from django.db import models
from tinymce import HTMLField
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250,null=True)
    content = HTMLField('Content')
    thumbnail = models.TextField()
    technologies = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.title

    def technologies_as_list(self):
        return self.technologies.split('\n') 