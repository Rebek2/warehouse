from django.forms import ModelForm
from django import forms
from parcelmanagement.models import Parcel,Customer




class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields=('price','product','description')

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'

class SenderForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'

