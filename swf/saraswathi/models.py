from django.db import models

# Create your models here.
class subjects(models.Model):

class users(models.Model):
    name=CharField(max_length=30,label=Username)
    email=EmailField(max_length=30,label=Email)
    


