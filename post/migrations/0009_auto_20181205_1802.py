# Generated by Django 2.1.3 on 2018-12-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20181205_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
