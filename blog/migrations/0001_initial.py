# Generated by Django 2.1.3 on 2018-12-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('banner', models.ImageField(upload_to='')),
            ],
        ),
    ]
