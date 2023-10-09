from django.db import models

# Create your models here.
class home(models.Model):
    productName = models.CharField(max_length=200)
    price =models.CharField(max_length=30)
    productImage=models.ImageField(upload_to='static/images/',default="")


class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=12)
    message=models.CharField(max_length=100)
# def __str__ (self):
#     return self.productName
# class freeCard(models.Model):
#     freeicon = models.ImageField(upload_to='static/images/',default="")
#     freetitle = models.CharField(max_length=30)
#     freelink = models.CharField(max_length=500)

