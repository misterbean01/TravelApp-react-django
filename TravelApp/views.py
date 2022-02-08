from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pymysql import NULL
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TravelApp.models import Travellers, Locations, Reviews
from TravelApp.serializers import TraverllerSerializers, LocationSerializers, ReviewSerializers

from django.core.files.storage import default_storage
# Create your views here.

# rest API
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def travellerApi(request, id=0):

    if request.method == 'GET':
        travellers = Travellers.objects.all()
        travellers_serializer = TraverllerSerializers(travellers, many=True)
        return Response(travellers_serializer.data)

    elif request.method == 'POST':
        traveller_data = JSONParser().parse(request)
        travellers_serializer = TraverllerSerializers(data=traveller_data)
        if travellers_serializer.is_valid():
            travellers_serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        traveller_data = JSONParser().parse(request)
        traveller_id_json = traveller_data['TravellerId']
        travellers = Travellers.objects.get(TravellerId=traveller_id_json)
        travellers_serializer = TraverllerSerializers(
            travellers, data=traveller_data)
        if travellers_serializer.is_valid() and (int(id) == traveller_id_json):
            travellers_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            traveller = Travellers.objects.get(TravellerId=id)
        except Travellers.DoesNotExist:
            return Response("Failed to Update", status=status.HTTP_404_NOT_FOUND)

        traveller.delete()
        return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def locationApi(request, id=0):
    if request.method == 'GET':
        locations = Locations.objects.all()
        locations_serializer = LocationSerializers(locations, many=True)
        return Response(locations_serializer.data)

    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        location_serializer = LocationSerializers(data=location_data)
        if location_serializer.is_valid():
            location_serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        location_data = JSONParser().parse(request)
        location_id_json = location_data['LocationId']
        locations = Locations.objects.get(LocationId=location_id_json)
        locations_serializer = LocationSerializers(
            locations, data=location_data)
        if locations_serializer.is_valid() and (int(id) == location_id_json):
            locations_serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            location = Locations.objects.get(LocationId=id)
        except Locations.DoesNotExist:
            return Response("Failed to Update", status=status.HTTP_404_NOT_FOUND)

        location.delete()
        return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)


# this needs to get the location ID so that it can get all the reviews associated with that location
@ api_view(['GET', 'POST', 'PUT', 'DELETE'])
def reviewApi(request, locId=0, revId=0):
    if request.method == 'GET':
        # reviews = Reviews.objects.all()
        reviews = Reviews.objects.all().filter(Location=locId)
        reviews_serializer = ReviewSerializers(reviews, many=True)
        return Response(reviews_serializer.data)

    elif request.method == 'POST':
        review_data = JSONParser().parse(request)
        review_serializer = ReviewSerializers(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        review_data = JSONParser().parse(request)
        review_id_json = review_data['ReviewId']
        reviews = Reviews.objects.get(ReviewId=review_id_json)
        reviews_serializer = ReviewSerializers(
            reviews, data=review_data)
        if reviews_serializer.is_valid() and (int(id) == review_id_json):
            reviews_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            review = Reviews.objects.get(ReviewId=id)
        except Reviews.DoesNotExist:
            return Response("Failed to Update", status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)
