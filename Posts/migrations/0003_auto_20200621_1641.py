# Generated by Django 3.0.6 on 2020-06-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20200620_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True, verbose_name='Slug/Link'),
        ),
    ]
