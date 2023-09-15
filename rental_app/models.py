from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.text import slugify
from multiselectfield import MultiSelectField



class Area(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # from rental_app.models import Area
    # areas = ['Banasree', 'Rampura', 'Dhanmondi', 'Azimpur', 'Mirpur']
    # objs = [Area(name=i) for i in areas]
    # Area.objects.bulk_create(objs)


class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # from rental_app.models import Area
    # areas = ['Banasree', 'Rampura', 'Dhanmondi', 'Azimpur', 'Mirpur']
    # objs = [Area(name=i) for i in areas]
    # Area.objects.bulk_create(objs)




class User(AbstractUser):
    ADMIN = 'A'
    LANDLORD = 'L'
    RENTER = 'R'
    ROLE_CHOICES = [
        (ADMIN,'Admin'),            
        (LANDLORD, 'Landlord'),
        (RENTER, 'Renter')
    ]
    
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=ADMIN)

    username_validator = ASCIIUsernameValidator()
    objects = UserManager()



class LanlordManager(models.Manager):
    def create_Landlord(self, first_name, last_name, phone_number, area, user):
        landlord = self.create(first_name=first_name, last_name=last_name, phone_number=phone_number, area=area, user=user)
        return landlord
        
    

class Landlord(models.Model):
    profile_image = models.ImageField(default="", blank=True, null=True, upload_to='profile/profile_images/')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    present_address = models.CharField(max_length=300, null=True, blank=True)
    permanent_address = models.CharField(max_length=300, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=False)

    objects = LanlordManager()


class RenterManager(models.Manager):
    def create_Renter(self, first_name, last_name, phone_number, area, user):
        renter = self.create(first_name=first_name, last_name=last_name, phone_number=phone_number, area=area, user=user)
        return renter


class Renter(models.Model):
    profile_image = models.ImageField(default="", blank=True, null=True, upload_to='profile/profile_images/')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    present_address = models.CharField(max_length=300, null=True, blank=True)
    permanent_address = models.CharField(max_length=300, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=False)

    objects = RenterManager()

class Rental_Property(models.Model):
    # FAMILY = 'F'
    # BACHELORS = 'B'
    # OFFICE = 'O'
    # RENTS_FOR = [
    #     (FAMILY,'For Family'),
    #     (BACHELORS,'For Bachelors'),
    #     (OFFICE,'For Office')
    # ]

    # YES_NO = [
    #     ('Y', 'YES'),
    #     ('N', 'NO')
    # ]

    # AVAILABLE = 'A'
    # NOTAVAILABLE = 'NA'

    # STATUS = [
    #     (AVAILABLE, 'Available'),
    #     (NOTAVAILABLE, 'Not Available')
    # ]

    title = models.CharField(max_length=300)
    slug = models.SlugField(default="", blank=True, editable=False, null=False)
    description = models.TextField()
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=20, null=True)
    rent_charge = models.PositiveIntegerField(default=0)
    rents_for = MultiSelectField(max_length=10, default='FAMILY')   # BACHELORS, OFFICE
    numbers_of_beds = models.PositiveSmallIntegerField()
    numbers_of_bath = models.PositiveSmallIntegerField()
    apartment_area = models.PositiveIntegerField(default=1)
    drawing_room_status = models.CharField(max_length=15, default='Available')
    dining_room_status = models.CharField(max_length=15, default='Available')
    kitchen_status = models.CharField(max_length=15, default='Available')
    rental_status = models.CharField(max_length=15, default='Available')        # Set default while posting
    electric_meter_type = models.CharField(max_length=10, default='Post-paid')
    gass_type = models.CharField(max_length=10, default='Pre-paid')
    post_date = models.DateField(auto_created=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
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


# class Renter_ProfileImage(models.Model):
#     image = models.ImageField()
#     Renter = models.OneToOneField(Renter, on_delete=models.CASCADE, primary_key=True)

# class Landlord_ProfileImage(models.Model):
#     image = models.ImageField()
#     Landlord = models.OneToOneField(Landlord, on_delete=models.CASCADE, primary_key=True)



class Transaction(models.Model):
    Renter = models.ForeignKey(Renter, on_delete=models.CASCADE, primary_key=False)
    Landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, primary_key=False)
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    trxID = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_created=True)


class Review(models.Model):
    Renter = models.ForeignKey(Renter, on_delete=models.CASCADE, primary_key=False)
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_created=True)


class Responses(models.Model):
    Renter = models.ForeignKey(Renter, on_delete=models.CASCADE, primary_key=False)
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)





class Bookmarks(models.Model):
    Renter = models.ForeignKey(Renter, on_delete=models.CASCADE, primary_key=False)
    Rental_Property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE, primary_key=False)


class Notification(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=False)
    Message = models.CharField(max_length=400)
