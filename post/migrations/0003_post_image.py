# Generated by Django 2.1.3 on 2018-11-29 14:36

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20181129_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.upload_image_path),
        ),
    ]
