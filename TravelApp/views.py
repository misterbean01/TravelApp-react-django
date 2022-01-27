from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TravelApp.models import Travellers, Locations, Reviews
from TravelApp.serializers import TraverllerSerializers, LocationSerializers, ReviewSerializers

from django.core.files.storage import default_storage
# Create your views here.


@csrf_exempt
def travellerApi(request, id=0):
    if request.method == 'GET':
        travellers = Travellers.objects.all()
        travellers_serializer = TraverllerSerializers(travellers, many=True)
        return JsonResponse(travellers_serializer.data, safe=False)

    elif request.method == 'POST':
        traveller_data = JSONParser().parse(request)
        travellers_serializer = TraverllerSerializers(data=traveller_data)
        if travellers_serializer.is_valid():
            travellers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        traveller_data = JSONParser().parse(request)
        travellers = Travellers.objects.get(
            TravellerId=traveller_data['TravellerId'])
        travellers_serializer = TraverllerSerializers(
            travellers, data=traveller_data)
        if travellers_serializer.is_valid():
            travellers_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':
        traveller = Travellers.objects.get(TravellerId=id)
        traveller.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def locationApi(request, id=0):
    if request.method == 'GET':
        locations = Locations.objects.all()
        locations_serializer = LocationSerializers(locations, many=True)
        return JsonResponse(locations_serializer.data, safe=False)

    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        location_serializer = LocationSerializers(data=location_data)
        if location_serializer.is_valid():
            location_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        location_data = JSONParser().parse(request)
        locations = Locations.objects.get(
            LocationId=location_data['LocationId'])
        locations_serializer = LocationSerializers(
            locations, data=location_data)
        if locations_serializer.is_valid():
            locations_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':
        location = Locations.objects.get(LocationId=id)
        location.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt  # this needs to get the location ID so that it can get all the reviews associated with that location
def reviewApi(request, locId=0, revId=0):
    if request.method == 'GET':
        #reviews = Reviews.objects.all()
        reviews = Reviews.objects.all().filter(Location=locId)
        reviews_serializer = ReviewSerializers(reviews, many=True)
        return JsonResponse(reviews_serializer.data, safe=False)

    elif request.method == 'POST':
        review_data = JSONParser().parse(request)
        review_serializer = ReviewSerializers(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        review_data = JSONParser().parse(request)
        reviews = Reviews.objects.get(
            ReviewId=review_data['ReviewId'])
        reviews_serializer = ReviewSerializers(
            reviews, data=review_data)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':
        review = Reviews.objects.get(ReviewId=revId)
        review.delete()
        return JsonResponse("Deleted Successfully", safe=False)
