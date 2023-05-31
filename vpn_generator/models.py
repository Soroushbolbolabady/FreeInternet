from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField()
    uuid = models.CharField(max_length=40)
    is_active = models.BooleanField(default=False)
