from django.db import models

# Create your models here.
class Menutext(models.Model):
    name = models.CharField(null=True, max_length=100)
    content = models.TextField(null=True)