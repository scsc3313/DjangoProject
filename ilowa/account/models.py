# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    profile_image = models.ImageField(upload_to='media/images/person/')
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '고객'
        verbose_name_plural = '고객 리스트'

    def __unicode__(self):
        return self.first_name + self.last_name
# Create your models here.
