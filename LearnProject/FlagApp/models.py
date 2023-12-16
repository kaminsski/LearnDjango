from django.db import models
from UserApp.models import *


class FlagModel(models.Model):
    name= models.CharField(("Name"), max_length=50)
    image=models.FileField(("Image"), upload_to="flags", max_length=100)
    capital=models.CharField(("Capital"), max_length=50)
    _id = models.IntegerField(("id"),null=True)
    flagPoint = models.IntegerField(("Flag Point"), null= True)

    def __str__(self):
        return self.name


class Records(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=("Record User"), on_delete=models.CASCADE)
    score = models.IntegerField(("Game score"))
    createdAt = models.DateTimeField(("createdAt"), auto_now_add=False, null=True, auto_now=True)
    
class Records1(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=("Record User"), on_delete=models.CASCADE)
    score = models.IntegerField(("Game score"))   
    createdAt = models.DateTimeField(("createdAt"),auto_now=True, auto_now_add=False , null=True) 


