from django.forms import ModelForm
from django import forms
from .models import Parcel,Customer


#Formularz do nadania przesyłki, jest do poprawy,
# bo nie umożliwia wpisania danych klientow, a jedynie wybrania z listy
class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields=('price','product','Receiver','Sender','description')
