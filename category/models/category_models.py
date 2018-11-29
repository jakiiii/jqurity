from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
