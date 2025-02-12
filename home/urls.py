from django.urls import path

from . import views

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
]
