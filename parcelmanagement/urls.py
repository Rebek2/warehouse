
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('parcels/',views.test_response,name = 'test_response'),
    path('nadaj/',views.dodaj,name = 'dodaj'),
    path('nadano/<str:number>/<int:pk>/',views.udaneNadanie,name = 'udaneNadanie'),
    path('szukaj/',views.search,name='search'),
    path('dodajstatus/',views.dodaj_status,name='dodaj_status'),
    path('dodajstatus/<int:pk>/<str:number>',views.status,name = 'dodajstatus'),
    path('parcel_pdf/<int:pk>/',views.list_przewozowy,name = 'list'),
    path('statystyki/',views.statystyki,name='statystyki'),



]
