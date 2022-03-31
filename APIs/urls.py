from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from APIs.views import event
from APIs.views.organiser import default,organisersList, organiserDetails, addOrganiser,updateOrganiser,deleteOrganiser

urlpatterns = [
    path("", default,name='default-api-view'),
    path("organisers/", organisersList,name='organisers-list'),
    path('organisers/<str:pk>',organiserDetails,name='organiser-details'),
    path("organisers/new/", addOrganiser,name='add-new-organiser'),
    path("organisers/update/<str:pk>", updateOrganiser,name='update-organiser'),
    path("organisers/delete/<str:pk>", deleteOrganiser,name='Delete-organiser'),

    path("events/",event.defaults, name = 'event-default')
]