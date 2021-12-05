
from django.shortcuts import render, redirect,get_object_or_404

from .forms import ParcelForm
from django.http import Http404

from .models import Parcel,Customer,ParcelStatus,Employee

#Testowanie views
def home(request):
    return render(request,'index.html')
def test_response(request):
    wszystkie = Parcel.objects.all()
    return render(request,'parcels.html',{'Przesyłki':wszystkie})



#Dodawanie/nadawanie przesyłek,
# może jakis redirect po nadaniu na wyświetlanie danych przesyłki(numer itp)??
def dodaj(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            Przesyłka = form.save()

        return redirect(udaneNadanie, Przesyłka.parcelnumber,Przesyłka.id)
    else:
        form = ParcelForm()
        return render(request, 'nadanie.html', {'form': form},)


def udaneNadanie(request,number,pk):
    parcel1  = get_object_or_404(Parcel, pk = pk,
                                 parcelnumber=number)

    return render(request, 'udaneNadanie.html', {'parcel1': parcel1}, )

def search(request):
    if request.method == "GET":
        query = request.GET.get('query')

        try:
            parcel = Parcel.objects.get(parcelnumber__exact = query)
            return redirect(udaneNadanie,parcel.parcelnumber,parcel.id)
        except:

            return render(request,'szukaj.html')