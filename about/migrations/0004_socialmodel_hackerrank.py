# Generated by Django 2.1.3 on 2018-12-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20181203_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmodel',
            name='hackerrank',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
    ]