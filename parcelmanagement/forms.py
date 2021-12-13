from django.forms import ModelForm
from django import forms
from parcelmanagement.models import Parcel,Customer,ParcelStatus


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


class StatusForm(forms.ModelForm):
    class Meta:
        model = ParcelStatus
        fields=('status_c','status_details','parcel_number')
class ParcelSForm(forms.Form):
    number = forms.CharField(max_length=100)

class StatusForm2(forms.ModelForm):
    class Meta:
        model = ParcelStatus
        fields=('status_c','status_details')