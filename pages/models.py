from django.db import models

# Create your models here.

class Company(models.Model):
    
    id = models.AutoField(blank=False,null=False,primary_key=True)
    company = models.TextField(blank=False,null=True)
    nation = models.TextField(blank=False,null=True)
   
    