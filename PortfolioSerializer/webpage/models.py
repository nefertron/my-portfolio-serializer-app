from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    mi = models.CharField(max_length=1)
    lname = models.CharField(max_length=100)
    bday = models.DateField()
    address = models.TextField()
    contact_no = models.CharField(max_length=11)
    image = models.TextField()
    email = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Introduction(models.Model):
    image = models.TextField()
    description1 = models.TextField(default=None, null=True, blank=True)
    description2 = models.TextField(default=None, null=True, blank=True)
    description3 = models.TextField(default=None, null=True, blank=True)
    description4 = models.TextField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.description}'

class Projects(models.Model):
    is_active = models.BooleanField(default=True)
    image = models.TextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    live_demo_link = models.TextField(default= 'https://github.com/', null=True, blank=True)
    source_code_link = models.TextField(default= 'https://github.com/', null=True, blank=True)

    def __str__(self):
        return f'TITLE : {self.title} || DESCRIPTION : {self.description}'


class Experiences(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'YEAR {self.year} || MONTH : {self.month} || TITLE : {self.title}'


class Languages(models.Model):
    image = models.TextField()
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class About(models.Model):
    image = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    resume_link = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.description}'


class Contact(models.Model):
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    email = models.TextField(default=None, blank=True, null=True)

    fb_link = models.TextField()
    messenger_link = models.TextField()
    gmail_link = models.TextField()
    twitter_link = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'ADDRESS : {self.address} || CONTACT NO : {self.contact_no}'


class Message(models.Model):
    sender = models.TextField()
    message = models.TextField()
    is_seen = models.BooleanField(default=False)
    date_send = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'SENDER : {self.sender} || MESSAGE : {self.message}'


