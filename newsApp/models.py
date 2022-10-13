from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=250, null=True)
    img = models.ImageField(null=True)
    date = models.DateField(null=True, auto_now_add=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
