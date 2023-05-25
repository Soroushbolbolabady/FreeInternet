from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField()
    config_url = models.URLField(max_length=800, blank=True)
    is_active = models.BooleanField(default=False)
