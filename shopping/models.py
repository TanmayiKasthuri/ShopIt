from django.db import models

# Create your models here.
class Attributes(models.Model):
    
    objname= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    sellername= models.CharField(max_length=100)
    price= models.IntegerField()
    desc= models.TextField()