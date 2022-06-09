from django.urls import path
from Home import views as home_views

urlpatterns = [
    path('', home_views.home, name='index'),
    path('contact', home_views.contact, name='contact'),
]
