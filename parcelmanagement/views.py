from django.shortcuts import render
from django.http import HttpResponse

from .models import Parcel,Customer,ParcelStatus,Employee
def test_response(request):
    wszystkie = Parcel.objects.all()
    return render(request,'parcels.html',{'Przesyłki':wszystkie})







