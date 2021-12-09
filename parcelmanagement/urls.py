
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('parcels/',views.test_response,name = 'test_response'),
    path('nadaj/',views.dodaj,name = 'dodaj'),
    path('nadano/<str:number>/<int:pk>/',views.udaneNadanie,name = 'udaneNadanie'),
    path('szukaj/',views.search,name='search'),



]
