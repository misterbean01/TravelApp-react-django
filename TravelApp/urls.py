from TravelApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path, path

urlpatterns = [
    # http://127.0.0.1:8000/traveller,
    re_path(r'^traveller/$', views.travellerApi),
    re_path(r'^traveller/([0-9]+)$', views.travellerApi),

    # http://127.0.0.1:8000/location
    re_path(r'^location/$', views.locationApi),
    re_path(r'^location/([0-9]+)$', views.locationApi),

    # http://127.0.0.1:8000/review
    re_path(r'^location/([0-9]+)/review/$', views.reviewApi),
    re_path(r'^location/([0-9]+)/review/([0-9]+)$', views.reviewApi),

    # http://127.0.0.1:8000/api
    #re_path(r'^api$', include('api.urls')),
    #path('', include('api.urls')),
]
