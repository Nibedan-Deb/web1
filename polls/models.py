from django.db import models

# Create your models here.
class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.TextField()