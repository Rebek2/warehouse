
from django.urls import path
from parcelmanagement.views import test_response,home
urlpatterns = [
    path('home/',home),
    path('home/parcels',test_response),


]
