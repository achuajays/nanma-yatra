from django.db import models

# Create your models here.



class s(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phno = models.CharField(max_length=100)
    po = models.CharField(max_length=100)
    do = models.CharField(max_length=100)
    dt = models.CharField(max_length=100)



class a(models.Model):
    d_n = models.CharField(max_length=100)
    c_n = models.CharField(max_length=100)
    t = models.TimeField()
    price = models.FloatField()


class dser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    v_no = models.CharField(max_length=20)
    phno = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class log(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()


# from django.db import models
# from django_google_maps.fields import MapField

# class MyModel(models.Model):
#     location = MapField()


class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_date = models.DateField(auto_now_add=True)
    product_or_service = models.CharField(max_length=200)
    rating = models.IntegerField()
    review_content = models.TextField()


from django.db import models
from django_google_maps.fields import AddressField, GeoLocationField

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = AddressField(max_length=200)
    geolocation = GeoLocationField(blank=True, null=True)

    def __str__(self):
        return self.name


from django.shortcuts import render
from .models import Location

def map_view(request):
    locations = Location.objects.all()
    context = {
        'locations': locations
    }
    return render(request, 'map.html', context)