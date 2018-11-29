from django.db import models
from .category_models import Category


# Create your models here.
class SubCategory(models.Model):
    sub_category = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_category
