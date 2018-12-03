# Generated by Django 2.1.3 on 2018-12-03 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0002_auto_20181129_1136'),
        ('category', '0003_auto_20181129_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=post.models.upload_image_path)),
                ('link', models.URLField(blank=True, max_length=300, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
