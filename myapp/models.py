from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("myapp:products")

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')
