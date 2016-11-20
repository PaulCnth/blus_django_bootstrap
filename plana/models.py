from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    keyword = models.CharField(max_length=30)
    abstract = models.CharField(max_length=200)
    date = models.DateTimeField('Insert time')

    def __unicode__(self):
        return self.title
