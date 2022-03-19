

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class regis(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    pswd = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    gst = models.CharField(max_length=20)
    contact = models.IntegerField(max_length=10)
    uname = models.CharField(max_length=20)
    def __str__(self):

        
         return self.fname +' '+ self.lname



class Profile(models.Model):

    regis=models.ForeignKey(regis,  on_delete=models.CASCADE,primary_key=True)
    companyname = models.CharField(max_length=20, default='noffne')
    ownername = models.CharField(max_length=20,default='noffne')
    bio = models.TextField(max_length=80,default='noffne')
    address = models.TextField(max_length=80,default='noffce')
    
    def __str__(self):
        return self.companyname +' '+ self.ownername





     