# Generated by Django 4.0.5 on 2022-06-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awapp', '0003_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='pics/'),
        ),
    ]
