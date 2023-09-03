# Generated by Django 4.2.4 on 2023-08-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='landlord',
            name='occupation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='renter',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
