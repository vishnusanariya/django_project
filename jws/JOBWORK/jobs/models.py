from email.policy import default
from tkinter import CASCADE
from django.db import models
from loginmodule.models import regis
from loginmodule.models import Profile
from django.core.files.storage import FileSystemStorage
import os

PRIVATE_DIR = os.path.join('.', 'static')
fs = FileSystemStorage(location=PRIVATE_DIR)

# Create your models here.
class jobs(models.Model):
    job_id=models.AutoField
    job_type=models.CharField(max_length=20)
    job_title=models.CharField(max_length=20)
    job_amount=models.IntegerField()
    job_description=models.CharField(max_length=300)
    job_duration=models.CharField(max_length=30)
    job_image=models.ImageField(upload_to='profile_pics')
    user=models.CharField(max_length=20,null=True)
    job_company=models.CharField(max_length=30,null=False,default='pvt.ltd')
    def __str__(self):
        return self.job_title

class History(models.Model):
    job_id=models.IntegerField()
    job_title=models.CharField(max_length=30,null=True)
    job_giver=models.CharField(max_length=30)
    job_worker=models.CharField(max_length=30)
    job_amount=models.IntegerField(null=False,default=00)
    def __str__(self):
        return self.job_giver +''+self.job_worker
    
class deal(models.Model):
    deal=models.ForeignKey(jobs,on_delete=models.CASCADE)
   #dealidd=models.IntegerField()
    status=models.BooleanField(default=False)
    job_worker=models.CharField(max_length=30)
    job_creater_approval=models.BooleanField(default=False)

    def __str__(self):
        return self.job_worker