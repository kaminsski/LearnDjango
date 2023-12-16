from django.db import models
from django.contrib.auth.models import AbstractUser

class ListeElemaniUser (models.Model):
    userListeElemaniMany = models.IntegerField(("Many") , null=True)
    
class ListeElemaniUser1 (models.Model):
    userListeElemaniMany = models.IntegerField(("Many") , null=True)    

class ListeElemaniMistake (models.Model):
    userListeElemaniMany = models.IntegerField(("Many") , null=True)    

class CustomUser(AbstractUser):
    avatar = models.FileField(("Avatar"), upload_to=None, max_length=100)
    userLastNumber = models.IntegerField(("User Last Number"), null=True, blank=True)
    userLastNumber1 = models.IntegerField(("User Last Number"), null=True, blank=True)    
    userListeElemani= models.ManyToManyField(ListeElemaniUser, verbose_name=("User Liste elemanı"))
    userListeElemani1= models.ManyToManyField(ListeElemaniUser1, verbose_name=("User Liste elemanı"))
    pointTotal = models.IntegerField(("Total Point"), default=0 , blank=True)
    gamePoint = models.IntegerField(("Game Point"),default=0, blank=True)
    gamePoint1 = models.IntegerField(("Game Point"),default=0, blank=True)
    firstStep= models.BooleanField(("first"), default=False)
    firstStep1= models.BooleanField(("first"), default=False)



    def __str__(self):
        return self.username