# Generated by Django 4.2.4 on 2023-09-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0008_alter_landlord_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]