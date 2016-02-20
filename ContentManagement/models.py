from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Pages(models.Model):
    Title = models.CharField(max_length=200, verbose_name="Page Title")
    # this is comment
    def __str__(self):
        return self.Title