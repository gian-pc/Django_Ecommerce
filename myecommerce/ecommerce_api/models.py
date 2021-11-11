from django.db import models
from django.utils.translation import activate

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Banner(models.Model):
    image = models.ImageField(upload_to = "banners", null = False)
    description = models.CharField(max_length=200)
    activated = models.BooleanField()

    def __str__(self):
        return self.description

class Brand(models.Model):
    image = models.ImageField(upload_to = "brands", null = False)
    brand = models.CharField(max_length = 200)
    activated = models.BooleanField()

    def __str__(self):
        return self.brand

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to = "products", null = False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    activated = models.BooleanField()
    
    def __str__(self):
        return self.name