from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_msg,name='hello_msg'),
    path('register_sample/',views.register_sample,name='register_sample'),
    path('register_franchesis/',views.register_franchesis,name="register_franchesis"),
    path('',views.franchesis_list,name="franchesis_list"),
    path('franchesis_get/<id>',views.franchesis_get,name="franchesis_get"),
    path('franchesis_delete/<id>',views.franchesis_delete,name="franchesis_delete"),
    path('franchesis_modelform/',views.franchesismodelform,name="franchesis_modelform"),
    path('franchesis_form/',views.franchesisform,name="franchesis_form")
]
