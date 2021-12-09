
from django.shortcuts import render, redirect,get_object_or_404

from .forms import ParcelForm, SenderForm, ReceiverForm
from django.http import Http404

from .models import Parcel,Customer

#Testowanie views
def home(request):
    return render(request,'index.html')
def test_response(request):
    wszystkie = Parcel.objects.all()
    return render(request,'parcels.html',{'Przesyłki':wszystkie})


#Dodawanie/nadawanie przesyłek,
def dodaj(request):

    if request.method == 'POST':
        sender = SenderForm(request.POST,prefix='sender')
        receiver= ReceiverForm(request.POST,prefix = 'receiver')
        form = ParcelForm(request.POST)
        if receiver.is_valid() and form.is_valid() and sender.is_valid() :
            Przesylka = form.save(commit = False)



            Przesylka.Receiver = receiver.save()
            Przesylka.Sender = sender.save()
            Przesylka.save()

        return redirect(udaneNadanie,Przesylka.parcelnumber,Przesylka.id)
    else:
        sender = SenderForm(prefix = 'sender')
        receiver = ReceiverForm(prefix = 'receiver')
        form = ParcelForm()
        return render(request, 'nadanie.html', {'form':form,'receiver':receiver,'sender':sender})





def udaneNadanie(request,number,pk):
    parcel1  = get_object_or_404(Parcel, pk = pk,
                                 parcelnumber=number)

    return render(request, 'udaneNadanie.html', {'parcel1': parcel1}, )

#szukanie przesylek
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')

        try:
            parcel = Parcel.objects.get(parcelnumber__exact = query)
            return redirect(udaneNadanie,parcel.parcelnumber,parcel.id)
        except:
            return render(request,'szukaj.html')