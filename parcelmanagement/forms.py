from django.forms import ModelForm
from django import forms
from .models import Parcel,Customer

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields='__all__'
