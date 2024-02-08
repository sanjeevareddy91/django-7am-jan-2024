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
        # 1st Approach
        # f_name = request.POST['f_name']
        # # if f_name
        # f_nickname = request.POST['f_nickname']
        # f_started_year = request.POST['f_started_year']
        # no_of_titles = request.POST['no_of_titles']
        # f_logo = request.FILES['f_logo']
        # print(f_name,f_nickname,f_started_year,no_of_titles,f_logo)
        # Franchesis.objects.create(f_name=f_name,f_nickname=f_nickname,f_started_year=f_started_year,no_of_titles=no_of_titles,f_logo=f_logo)
        # 2nd Approach
        data = {ele:request.POST[ele] for ele in request.POST if ele!='csrfmiddlewaretoken'}
        data.update({'f_logo':request.FILES['f_logo']})
        Franchesis.objects.create(**data)
        print(data)
        return HttpResponse("Franchesis Registered Successfully!")
    return render(request,'register_franchesis.html')

def franchesis_list(request):
    franchesis_list = Franchesis.objects.all()
    # print(franchesis_list)
    return render(request,'franchesis_list.html',{'franchesis':franchesis_list})


def franchesis_get(request,id):
    # 1st Approach
    # franchesis = Franchesis.objects.get(id=id)
    # if request.method == "POST":
    #     franchesis.f_name = request.POST['f_name']
    #     franchesis.f_nickname = request.POST['f_nickname']
    #     franchesis.f_started_year = request.POST['f_started_year']
    #     franchesis.no_of_titles = request.POST['no_of_titles']
    #     franchesis.save()
    #     return HttpResponse("Data Updated")
    # 2nd Approach
    franchesis = Franchesis.objects.filter(id=id)
    if request.method == "POST":
        data = {ele:request.POST[ele] for ele in request.POST if ele!='csrfmiddlewaretoken'}
        if request.FILES.get('f_logo'):
            data.update({'f_logo':request.FILES['f_logo']})
        franchesis.update(**data)
        return HttpResponse("Data Updated")
    return render(request,'franchesis_update.html',{'franchesis':franchesis[0]})

def franchesis_delete(request,id):
    franchesis = Franchesis.objects.get(id=id)
    franchesis.delete()
    return HttpResponse("Data Deleted")


# ModelForms
# Normalforms

from .forms import FranchesisModelForm, FranchesisForm
def franchesismodelform(request):
    form = FranchesisModelForm()
    if request.method=="POST":
        form = FranchesisModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Record Created")
    return render(request,'register_franchesismodelform.html',{'form':form})

def franchesisform(request):
    form = FranchesisForm()
    return render(request,'franchesis_form.html',{'form':form})