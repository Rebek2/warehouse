from django.forms import ModelForm
from django import forms
from parcelmanagement.models import Parcel,Customer,ParcelStatus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields=('price','product','description')
        labels={
            'price':'Wartość przesyłki[zł]',
            'product':'Typ przesyłki',
            'description':'Szczegóły',
        }


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        labels={
            'name':'Imię',
            'phone':'Telefon',
            'EmailAdress':'Adres Email',
            'Street': 'Ulica',
            'PostalCode':'Kod pocztowy',
            'City':'Miasto',


        }


class SenderForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        labels={
            'name':'Imię',
            'phone':'Telefon',
            'EmailAdress':'Adres Email',
            'Street': 'Ulica',
            'PostalCode':'Kod pocztowy',
            'City':'Miasto',


        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = ParcelStatus
        fields=('status_c','status_details','parcel_number')
        labels={
            'status_c':'Status',
            'status_details':'Opis',
            'parcel_number':'Numer przesyłki',
        }


class ParcelSForm(forms.Form):
    number = forms.CharField(max_length=100)

class StatusForm2(forms.ModelForm):
    class Meta:
        model = ParcelStatus
        fields=('status_c','status_details')
        labels={
            'status_c':'Status',
            'status_details':'Opis',
        }


class ParcelprzForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ('description',)
        labels={
            'description':'Opis przesyłki',
        }

#Rejestrowanie, nie wiem czy uzywac: tylko admin bedzie mogl rejestrować uzytkownikow lub klient będzie mógl sie zarejestrowac i jedynie nadac i przegladac przesylki.
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']