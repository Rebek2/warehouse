import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#Model klienta - może to być nadawca albo odbiorca w zależności,
# gdzie ulokowany jest w relacji z modelem Parcel
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    EmailAdress = models.EmailField(blank = True)
    Street = models.CharField(max_length = 30)
    PostalCode = models.BigIntegerField()
    City = models.CharField(max_length=100)


    def __str__(self):
        str(self.PostalCode)
        return("{}  {}  {}  {}".format(self.name,self.PostalCode,self.City,self.Street))



#Status przesyłek (w relacji many to one czyli wiele statusów do 1 przesyłki),
# które będzie mógł aktualizować pracownik, będą wyświetlane od najnowszego do najstarszego
class ParcelStatus(models.Model):
    STATUS_CHOICE = (("01 : Nadano","01 : Nadano"),
                     ("02 : W drodze","02 : W drodze"),
                     ("03 : Uszkodzona","03 : Uszkodzona"),
                     ("04 : Zniszczona całkowicie","04 : Zniszczona całkowicie"),
                     ("05 : Dostarczona","05 : Dostarczona"),
                     ("06 : Błąd adresu","06 : Błąd adresu"),
                     ("07 : Pozostawiona w magazynie","07 : Pozostawiona w magazynie"),
                     ("08 : W trakcie wyjaśniania","08 : W trakcie wyjaśniania",),
                     ("09 : Przekierowana","09 : Przekierowana", ),)

    status_c = models.CharField(max_length=300,choices=STATUS_CHOICE)
    status_details = models.CharField(max_length=200, blank=True)
    dateStatus = models.DateTimeField(auto_now_add=True)
    added = models.CharField(max_length=100)
    parcel_number = models.ForeignKey('Parcel', on_delete=models.CASCADE)
    class Meta:
        ordering = ('-dateStatus','parcel_number')

    def __str__(self):
        return str(f'{self.parcel_number} {self.status_c}')
#Model samej przesyki gdzie generowany jest numer przesyłki UUID - można później zmienić
#Sender i Receiver - odbiorca i nadawca w relacji one to many - jeden klient moze byc przypisany do wielu przesylek
class Parcel(models.Model):
    CATEGORY = (
        ("Niestandardowa" , "Niestandardowa"),
        ("Standardowa" , "Standardowa"),
        )
    parcelnumber = models.UUIDField(default = uuid.uuid4,unique = True,editable=False)
    price = models.FloatField(null = True)
    product = models.CharField(max_length=200,null=True,choices=CATEGORY)
    Sender = models.ForeignKey(Customer,on_delete=models.PROTECT,related_name='sender')
    Receiver = models.ForeignKey(Customer,on_delete = models.PROTECT,related_name='receiver')
    description = models.CharField(max_length=300,null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created',)



    #def get_absolute_url(self):
        #return reverse('parcelmanagement.views.status',args = [self.parcelnumber,
                               #self.id])


    def __str__(self):
        return (str(self.parcelnumber))

#Model pracownika !!do rozwinięcia!!
class Employee(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name


