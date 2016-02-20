from __future__ import unicode_literals

from django.db import models

class Pages(models.Model):
    Title = models.CharField(max_length=200, verbose_name='Pages Title')

# Create your models here.
