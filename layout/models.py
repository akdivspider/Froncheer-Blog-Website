from os import name
from pyexpat import model
from django.db import models

class Heading(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    

    


class Topic(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img =  models.ImageField(upload_to = 'pics')
    tags = models.TextField()
    



