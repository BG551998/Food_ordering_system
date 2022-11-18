from django.db import models

# Create your models here.

class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    adress =models.CharField(max_length=200)

    def __str__(self):
        return self.fullname


# creating models for food items

class FOODITEMS(models.Model):
    name=models.CharField(max_length=30)  
    desc=models.CharField(max_length=300)
    price=models.IntegerField(blank=True, null=True) 
    food_image=models.ImageField(upload_to ='uploads/') 


def __str__(self):
        return self.fullname
