# Generated by Django 4.2.4 on 2023-08-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0004_remove_renter_profileimage_renter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='profile_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_images/'),
        ),
    ]
