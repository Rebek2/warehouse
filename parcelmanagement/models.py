import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#modele danych
class Customer(models.Model):
    name = models.CharField(max_length=200,null = True)
    phone = models.CharField(max_length=11, null = True)
    Adress = models.CharField(max_length = 40, null = True)
    Street = models.CharField(max_length = 30, null=True)
    PostalCode = models.BigIntegerField(null=True)
    City = models.CharField(max_length=100,null=True)


    def __str__(self):
        str(self.PostalCode)
        return("{}  {}  {}  {}".format(self.name,self.PostalCode,self.City,self.Street))

class ParcelStatus(models.Model):
    STATUS_CHOICE = (("Nadano","Nadano"),
                     ("W drodze","W drodze"),
                     ("Uszkodzona","Uszkodzona"),
                     ("Zniszczona całkowicie","Zniszczona całkowicie"),
                     ("Dostarczona","Dostarczona"),
                     ("Błąd adresu","Błąd adresu"),
                     ("Pozostawiona na magazynie","Pozostawiona na magazynie"),
                     ("W trakcie wyjaśniania","W trakcie wyjaśniania",))

    status_c = models.CharField(max_length=300,choices=STATUS_CHOICE,default = "Nadano")
    status_details = models.CharField(max_length=200, null=True,blank=True)
    dateStatus = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    parcel_number = models.ForeignKey('Parcel', on_delete=models.CASCADE)
    def __str__(self):
        return str(f'{self.parcel_number} {self.status_c}')
class Parcel(models.Model):
    CATEGORY = (
        ("Niestandardowa" , "Niestandardowa"),
        ("Standardowa" , "Standardowa"),
        )
    parcelnumber = models.UUIDField(default = uuid.uuid4,unique = True,editable=False)
    price = models.FloatField(null = True)
    product = models.CharField(max_length=200,null=True,choices=CATEGORY)
    Sender = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='sender')
    Receiver = models.ForeignKey(Customer,on_delete = models.CASCADE,related_name='receiver')
    description = models.CharField(max_length=300,null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return (str(self.parcelnumber))


class Employee(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name


