from django.db import models

# Create your models here.

#from users.models import user

class product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='products_image')
    price = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    quantity = models.PositiveIntegerField(default=0)
    dateOfCreation = models.DateTimeField(auto_now=True)
    # auto_now=False, default 0 and updates when arg update
    dateOfUpdate = models.DateTimeField(auto_now=True)
    # creator is a imported user!
    creator = models.CharField(max_length=50)