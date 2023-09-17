# Generated by Django 4.2.4 on 2023-09-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0017_rename_bookmarks_bookmark_alter_property_image_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_property',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=500),
        ),
        migrations.AlterField(
            model_name='rental_property',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
