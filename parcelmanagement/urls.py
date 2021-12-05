
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home),
    path('parcels/',views.test_response),
    path('nadaj/',views.dodaj),
    path('nadano/<str:number>/<int:pk>/',views.udaneNadanie,name = 'udaneNadanie'),
    path('szukaj/',views.search,name='search'),


]
