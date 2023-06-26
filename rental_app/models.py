from django.db import models
from django.utils.text import slugify

class User(models.Model):
    ADMIN = 'A'
    LANDLORD = 'LL'
    RENTER = 'R'
    ROLE_CHOICES = [
        (ADMIN,'Admin'),            # maybe no need
        (LANDLORD, 'Landlord'),
        (RENTER, 'Renter')
    ]

    # user_id = models.SmallIntegerField(auto_created=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=RENTER)


class Landlord(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0)
    present_address = models.CharField(max_length=300)
    permanent_address = models.CharField(max_length=300)
    User = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=False)

class Renter(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0)
    present_address = models.CharField(max_length=300)
    permanent_address = models.CharField(max_length=300)
    occupation = models.CharField(max_length=100)
    User = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=False)


class Rental_Property(models.Model):
    FAMILY = 'F'
    BACHELORS = 'B'
    OFFICE = 'O'
    RENTS_FOR = [
        (FAMILY,'For Family'),
        (BACHELORS,'For Bachelors'),
        (OFFICE,'For Office')
    ]

    YES_NO = [
        ('Y', 'YES'),
        ('N', 'NO')
    ]

    AVAILABLE = 'A'
    NOTAVAILABLE = 'NA'

    STATUS = [
        (AVAILABLE, 'Available'),
        (NOTAVAILABLE, 'Not Available')
    ]

    title = models.CharField(max_length=300)
    slug = models.SlugField(default="", blank=True, null=False)
    description = models.TextField()
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=20, null=True)
    rents_for = models.CharField(max_length=2, choices=RENTS_FOR, default=FAMILY)
    numbers_of_beds = models.PositiveSmallIntegerField()
    numbers_of_bath = models.PositiveSmallIntegerField()
    drawing_room_status = models.CharField(max_length=3, choices=STATUS, default=AVAILABLE)
    dining_room_status = models.CharField(max_length=3, choices=STATUS, default=AVAILABLE)
    kitchen_status = models.CharField(max_length=3, choices=STATUS, default=AVAILABLE)
    rental_status = models.CharField(max_length=3, choices=STATUS, default=AVAILABLE)
    post_date = models.DateField(auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)
    Landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, primary_key=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Property_Image(models.Model):
    image = models.ImageField()
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)

class Services(models.Model):
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)
    service_type = models.CharField(max_length=100)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)


class Renter_ProfileImage(models.Model):
    image = models.ImageField()
    Renter = models.OneToOneField(Renter, on_delete=models.CASCADE, primary_key=True)

class Landlord_ProfileImage(models.Model):
    image = models.ImageField()
    Landlord = models.OneToOneField(Landlord, on_delete=models.CASCADE, primary_key=True)



class Transaction(models.Model):
    Renter = models.ForeignKey(Renter, on_delete=models.CASCADE, primary_key=False)
    Landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, primary_key=False)
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    trxID = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_created=True)


class Review(models.Model):
    Renter = models.OneToOneField(Renter, on_delete=models.CASCADE, primary_key=False)
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_created=True)

