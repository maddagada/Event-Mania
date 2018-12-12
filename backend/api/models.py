from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
from django.core import serializers
#from rest_framework import serializers
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class Product(models.Model):
    name = models.CharField(max_length=30, blank=False)
    price = models.IntegerField()
    period = models.CharField(max_length=6, blank=False)
    color = models.CharField(max_length=10, blank=False)
    category = models.CharField(max_length=10, default='chairs', blank=False)
    imagesrc = models.CharField(max_length=50, default='/static/ember/c1.jpg', blank=False)

    def __str__(self):
        return str(self.name)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')
