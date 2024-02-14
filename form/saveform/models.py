from django.db import models

# Create your models here.
class stdent_data(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    joining_date=models.DateField()
    course=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    duration=models.CharField(max_length=50)
class attendence(models.Model):
    topic=models.CharField(max_length=50)
    Date=models.DateField()
    intime=models.TimeField()
    outtime=models.TimeField()
    message=models.TextField()
    
    