from django.db import models

# Create your models here.


class Travellers(models.Model):
    TravellerId = models.AutoField(primary_key=True)
    TravellerFirstName = models.CharField(max_length=500)
    TravellerLastName = models.CharField(max_length=500)
    TravellerBio = models.CharField(max_length=500, default="")


class Locations(models.Model):
    LocationId = models.AutoField(primary_key=True)
    LocationName = models.CharField(max_length=500)
    LocationsDescription = models.CharField(max_length=500)
    LocationsGPS = models.CharField(max_length=500)
    PhotoFileName = models.CharField(max_length=500)


class Reviews(models.Model):
    ReviewId = models.AutoField(primary_key=True)
    ReviewContent = models.CharField(max_length=500)
    ReviewDate = models.DateField()
    ReviewRating = models.IntegerField()
    Traveller = models.ForeignKey(Travellers, on_delete=models.DO_NOTHING)
    Location = models.ForeignKey(Locations, on_delete=models.DO_NOTHING)
