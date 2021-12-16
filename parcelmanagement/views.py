from barcode import Code128
from django.shortcuts import render, redirect,get_object_or_404
from barcode.writer import ImageWriter
from .forms import ParcelForm, SenderForm, ReceiverForm,StatusForm,StatusForm2
from .models import Parcel,Customer, ParcelStatus
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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
            status = ParcelStatus(status_c= 'Nadano',status_details='Nadana przez aplikacje webowa' ,parcel_number_id = Przesylka.id)
            status.save()
        return redirect(udaneNadanie,Przesylka.parcelnumber,Przesylka.id)
    else:
        sender = SenderForm(prefix = 'sender')
        receiver = ReceiverForm(prefix = 'receiver')
        form = ParcelForm()
        return render(request, 'nadanie.html', {'form':form,'receiver':receiver,'sender':sender})


def udaneNadanie(request,number,pk):
    parcel1  = get_object_or_404(Parcel, pk = pk,
                               parcelnumber=number)
    statusy = ParcelStatus.objects.all().filter(parcel_number=parcel1.id)
    return render(request, 'udaneNadanie.html', {'parcel1': parcel1,'statusy':statusy}, )

#szukanie przesylek
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        try:
            parcel = Parcel.objects.get(parcelnumber__exact = query)
            return redirect(udaneNadanie,parcel.parcelnumber,parcel.id)
        except:
            query = request.GET.get('query')
            return render(request,'szukaj.html')


def dodaj_status(request):
    if request.method == 'POST':
        status = StatusForm(request.POST)
        if status.is_valid():
            status.save()


            return redirect(dodaj_status)
    else:
        status=StatusForm()
        return render(request,'status.html',{'status':status})



def status(request,pk,number):
    if request.method == 'POST':
        form = StatusForm2(request.POST)
        parcel = get_object_or_404(Parcel, pk=pk,parcelnumber = number)
        if form.is_valid():
            statusik = form.save(commit=False)
            statusik.parcel_number = parcel
            statusik.save()
        return redirect(udaneNadanie,parcel.parcelnumber,parcel.id)

    else:
        form = StatusForm2()
        parcel = get_object_or_404(Parcel, pk=pk, parcelnumber=number)
        return render(request,'statusUD.html',{'form':form,'parcel':parcel})



def list_przewozowy(request,pk):
    parcel = get_object_or_404(Parcel,pk=pk)
    template_path = 'listprzewozowy.html'
    code = str(parcel.parcelnumber)
    number1 = Code128(code,writer=ImageWriter())
    number = number1.save('barkod')
    context = {'parcel':parcel,'number':number}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="listprzewozowy.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def statystyki(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if request.GET.get('query')!= None:
            data = ParcelStatus.objects.all().filter(status_c__contains=query).order_by('-dateStatus')
            ilosc = len(data)
            status = query
            return render(request,'info.html',{"data":data,"ilosc":ilosc,'status':status})
        return render(request, 'stats.html')
