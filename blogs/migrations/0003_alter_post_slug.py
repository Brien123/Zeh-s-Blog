# Generated by Django 5.0.3 on 2024-07-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_authoor_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique_for_date='publish'),
        ),
    ]
