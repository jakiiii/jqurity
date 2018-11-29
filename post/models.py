import os
import random

from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.core.files.storage import FileSystemStorage

from category.models import Category
from tags.models import Tag

from jqurity.utils import unique_slug_generator
fs = FileSystemStorage(location='media')


def get_filename_exist(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(inistance, file_name):
    new_filename = random.randint(1, 101119)
    name, ext = get_filename_exist(file_name)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


User = settings.AUTH_USER_MODEL


# Create your queryset here.
class PostQuerySet(models.QuerySet):
    pass


# Create your manager here.
class PostManager(models.Manager):
    pass


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    link = models.URLField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)

    objects = PostManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
        # return "/products/{slug}".format(slug=self.slug)
        # return reverse("product-detail", kwargs={"slug": self.slug})


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Post)
