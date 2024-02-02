from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_msg,name='hello_msg'),
    path('register_sample/',views.register_sample,name='register_sample'),
    path('register_franchesis/',views.register_franchesis,name="register_franchesis"),
    path('franchesis_list/',views.franchesis_list,name="franchesis_list")
]
