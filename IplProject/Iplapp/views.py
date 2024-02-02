from django.shortcuts import render
from django.http import HttpResponse
from Iplapp.models import Franchesis
# Create your views here.

# Function Based Views.

def hello_msg(request):
    return HttpResponse("<h1>Hello World<h2>")

def register_sample(request):
    return render(request,'register_sample.html')

def register_franchesis(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        f_name = request.POST['f_name']
        # if f_name
        f_nickname = request.POST['f_nickname']
        f_started_year = request.POST['f_started_year']
        no_of_titles = request.POST['no_of_titles']
        f_logo = request.FILES['f_logo']
        print(f_name,f_nickname,f_started_year,no_of_titles,f_logo)
        Franchesis.objects.create(f_name=f_name,f_nickname=f_nickname,f_started_year=f_started_year,no_of_titles=no_of_titles,f_logo=f_logo)
        return HttpResponse("Franchesis Registered Successfully!")
    return render(request,'register_franchesis.html')