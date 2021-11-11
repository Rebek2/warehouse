from django.contrib import admin
from .models import Parcel,ParcelStatus,Customer,Employee

admin.site.register(Customer)

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('parcelIDD','Sender','Receiver','product','price','created')
admin.site.register(ParcelStatus)

admin.site.register(Employee)