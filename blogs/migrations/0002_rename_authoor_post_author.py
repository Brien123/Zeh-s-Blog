# Generated by Django 5.0.3 on 2024-07-22 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authoor',
            new_name='author',
        ),
    ]
