from django.db import models

# Create your models here.
class home(models.Model):
    productName = models.CharField(max_length=200)
    price =models.CharField(max_length=30)
    productImage=models.ImageField(upload_to='static/images/',default="")

# def __str__ (self):
#     return self.productName
# class freeCard(models.Model):
#     freeicon = models.ImageField(upload_to='static/images/',default="")
#     freetitle = models.CharField(max_length=30)
#     freelink = models.CharField(max_length=500)

