from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from PIL import Image
import datetime
from django.core.validators import MaxValueValidator
# from django.conf import settings
# User = settings.AUTH_USER_MODEL

# import geocoder

# Create your models here.

class Division(models.Model):
    division_name = models.CharField(max_length=50)

    def __str__(self):
        return self.division_name


class Locality(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    locality_name = models.CharField(max_length=100)
    post_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.locality_name


class PostalCode(models.Model):
    post_code = models.IntegerField()
    neighbouring_area = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.post_code)


class Garage(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='garage')
    garage_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=False)
    other_number = models.CharField(max_length=15, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='garage')
    description = models.CharField(max_length=500, blank=False, default='No description')
    photo = models.ImageField(upload_to='garage_photos', blank=False)
    PLACE_CATEGORY_CHOICE = (
        ("Commercial", "Commercial"),
        ("Residential", "Residential"),
    )
    place_category = models.CharField(max_length=20, choices=PLACE_CATEGORY_CHOICE, default="Commercial")
    bike_slot = models.IntegerField(default=0)
    car_slot = models.IntegerField(default=0)
    bicycle_slot = models.IntegerField(default=0)
    allow_monthly = models.BooleanField(default=True)
    monthly_cost = models.FloatField(default=0)
    allow_hourly = models.BooleanField(default=True)
    hourly_cost = models.FloatField(default=0)
    allow_daily = models.BooleanField(default=True)
    daily_cost = models.FloatField(default=0) 
    opening_time = models.TimeField()
    close_time = models.TimeField()
    CCTV = models.BooleanField(default=False)
    Gaurd = models.BooleanField(default=False)
    Indoor = models.BooleanField(default=False)

    location = models.CharField(max_length=100)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    time = datetime.datetime.now()
    
    rating = models.IntegerField(default=0)
    ratingCount = models.IntegerField(default=0)
    avgRating = models.FloatField(default=0)

    postalCode = models.ForeignKey(PostalCode, on_delete=models.CASCADE, default=1)


    def save(self,*args, **kwargs): 
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height < img.width :
            img.rotate(90)
        if img.height > 480 or img.width > 640 or img.height < 480 or img.width < 640:
            output_size = (480 , 640)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        return self.garage_name


class Booking(models.Model):
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, related_name='booking')    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_owner')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_customer')

    customer_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    vehice_number = models.CharField(max_length=50)
    VEHICLE_TYPE_CHOICE = (("Bike", "Bike"), ("Car", "Car"), ("Bicycle", "Bicycle"))
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICE, default="Car")
    image_of_necesssary_papers = models.ImageField(upload_to='Booking_document', blank=True, null=True)
    
    status = models.IntegerField(default=0) 
    #[ 0 = pending, 1 = accepted, 2 = rejected, 3 = completed, 4 = cancelled, 5 = paymentPending, 6 = paymentCompleted, 7 = reviewCompleted]

    BOOKING_TYPE_CHOICE = (
        ("Hour", "Hour"),
        ("Day", "Day"),
        ("Month", "Month"),
    )
    type_of_booking = models.CharField(max_length=20, choices=BOOKING_TYPE_CHOICE, default="Hour")
    booking_quantity = models.IntegerField(default=1)
    start_time = models.CharField(max_length=25)
    start_date = models.CharField(max_length=25)	
    time = models.DateTimeField(auto_now_add=True)

    totalAmount = models.FloatField(default=0)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.garage.garage_name


class CustomerReview(models.Model):
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, related_name='review')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_customer')
    review = models.CharField(max_length=500, blank=True, null=True)
    # MIN_INT = 0
    # MAX_INT = 5
    # rating = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.garage.garage_name + "|" + self.customer.username

