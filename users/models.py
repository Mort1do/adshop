from django.db import models
from django.contrib.auth.models import AbstractUser

# HERE WILL BE ORM MODELS USER

# NOW ITS EXAMPLE
class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=True, blank=True)


