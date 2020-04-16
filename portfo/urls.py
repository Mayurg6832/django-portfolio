from django.contrib import admin
from django.urls import path,include
from portfo import views

app_name = 'portfo'

urlpatterns = [
    path('about/', views.about,name='about_me'),
    path('contact/',views.contact,name='contact'),
    path('get_value/',views.get_value,name='get_value'),
]