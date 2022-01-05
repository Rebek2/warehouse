from barcode import Code128
from django.shortcuts import render, redirect,get_object_or_404
from barcode.writer import ImageWriter
from .forms import ParcelForm, SenderForm, ReceiverForm,StatusForm,StatusForm2,ParcelprzForm
from .models import Parcel,Customer, ParcelStatus

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

#login i logout
def loginPage(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Login lub hasło są nieprawidłowe ')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect(login)







#Testowanie views
@login_required(login_url='login')
def home(request):
    return render(request,'index.html')
@login_required(login_url='login')
def test_response(request):
    wszystkie = Parcel.objects.all()
    return render(request,'parcels.html',{'Przesyłki':wszystkie})


#Dodawanie/nadawanie przesyłek,
@login_required(login_url='login')
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
            status = ParcelStatus(status_c= '01 : Nadano',status_details='Nadana przez aplikacje webowa' ,parcel_number_id = Przesylka.id,added = request.user)
            status.save()
        return redirect(udaneNadanie,Przesylka.parcelnumber,Przesylka.id)
    else:
        sender = SenderForm(prefix = 'sender')
        receiver = ReceiverForm(prefix = 'receiver')
        form = ParcelForm()
        return render(request, 'nadanie.html', {'form':form,'receiver':receiver,'sender':sender})

@login_required(login_url='login')
def udaneNadanie(request,number,pk):
    parcel1  = get_object_or_404(Parcel, pk = pk,
                               parcelnumber=number)
    statusy = ParcelStatus.objects.all().filter(parcel_number=parcel1.id)
    return render(request, 'udaneNadanie.html', {'parcel1': parcel1,'statusy':statusy}, )

#szukanie przesylek
@login_required(login_url='login')
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        try:
            parcel = Parcel.objects.get(parcelnumber__exact=query)
            return redirect(udaneNadanie,parcel.parcelnumber,parcel.id)
        except:
            if query is not None:
                messages.info(request, 'Brak przesyłki o numerze: {}'.format(query))
            return render(request,'szukaj.html')

    else:
        return render(request,'szukaj.html')

@login_required(login_url='login')
def dodaj_status(request):
    if request.method == 'POST':
        status = StatusForm(request.POST)
        if status.is_valid():
            y = status.save(commit = False)
            y.added = request.user
            y.save()
            return redirect(dodaj_status)
    else:
        status=StatusForm()
        return render(request,'status.html',{'status':status})


@login_required(login_url='login')
def status(request,pk,number):
    if request.method == 'POST':
        form = StatusForm2(request.POST)
        parcel = get_object_or_404(Parcel, pk=pk,parcelnumber = number)
        if form.is_valid():
            statusik = form.save(commit=False)
            statusik.added = request.user
            statusik.parcel_number = parcel
            statusik.save()
        return redirect(udaneNadanie,parcel.parcelnumber,parcel.id)

    else:
        form = StatusForm2()
        parcel = get_object_or_404(Parcel, pk=pk, parcelnumber=number)
        return render(request,'statusUD.html',{'form':form,'parcel':parcel})


@login_required(login_url='login')
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


@login_required(login_url='login')
def statystyki(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if request.GET.get('query')!= None:
            data1 = ParcelStatus.objects.all().filter(status_c__contains=query).order_by('-dateStatus')


            ilosc = len(data1)
            status = query
            return render(request,'info.html',{"data":data1,"ilosc":ilosc,'status':status})

        return render(request, 'stats.html')

@login_required(login_url='login')
def szukaj_prz(request):
    if request.method == "GET":
        query = request.GET.get('query')

        try:
            parcel = Parcel.objects.get(parcelnumber__exact=query)
            return redirect(przekierowanie, parcel.parcelnumber, parcel.id)
        except:
            if query is not None:
                messages.info(request, 'Brak przesyłki o numerze: {} w bazie danych!'.format(query))
            return render(request, 'szukajprzek.html')
    else:
        return render(request, 'szukajprzek.html')

@login_required(login_url='login')
def przekierowanie(request,number,pk):
    parcel = get_object_or_404(Parcel,pk=pk,parcelnumber = number)

    if request.method == "POST":
        parcel1 = Parcel()
        receiver = ReceiverForm(request.POST,prefix = 'receiver')
        if receiver.is_valid():

            parcel1.Receiver = receiver.save()
            parcel1.Sender = parcel.Sender
            parcel1.price = parcel.price
            parcel1.product = parcel.product
            parcel1.description = parcel.description

            parcel1.save()
            status = ParcelStatus(status_c= '09 : Przekierowano',
                                  status_details='Przekierowana przez aplikacje webowa do {}'.format(parcel1.parcelnumber)
                                  ,parcel_number_id = parcel.id)
            status.save()
            status1 = ParcelStatus(status_c= '01 : Nadano',
                                   status_details='Nadana przez aplikacje webowa (przekierowana z {})'.format(parcel.parcelnumber)
                                   ,parcel_number_id = parcel1.id)
            status1.save()
        return redirect(udaneNadanie, parcel1.parcelnumber, parcel1.id)
    else:

        receiver = ReceiverForm(prefix='receiver')
        return render(request, 'przekierowanie.html',{'receiver':receiver,})