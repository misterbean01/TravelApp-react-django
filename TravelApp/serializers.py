from rest_framework import serializers
from TravelApp.models import Travellers, Locations, Reviews


class TraverllerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Travellers
        fields = ('TravellerId', 'TravellerFirstName',
                  'TravellerLastName', 'TravellerBio')


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('LocationId', 'LocationName',
                  'LocationsDescription', 'LocationsGPS',
                  'PhotoFileName')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('ReviewId', 'ReviewContent',
                  'ReviewDate', 'ReviewRating',
                  'Traveller', 'Location')
