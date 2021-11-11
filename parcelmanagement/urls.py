
from django.urls import path
from parcelmanagement.views import test_response
urlpatterns = [
    path('test/',test_response),


]
