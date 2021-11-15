from django.shortcuts import render
from django.http import HttpResponse
from .forms import ParcelForm

from .models import Parcel,Customer,ParcelStatus,Employee
def home(request):
    return render(request,'index.html')
def test_response(request):
    wszystkie = Parcel.objects.all()
    return render(request,'parcels.html',{'Przesyłki':wszystkie})


def dodaj(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():

            form.save()
            return render(request,'nadanie.html',{'form':form},)

    else:
        form = ParcelForm()
    return render(request, 'nadanie.html', {'form': form},)



