from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth import authenticate ,login ,logout
from django.urls import reverse
from .models import FOODITEMS



# Create your views here.
def render_login(request):
    return render(request, "login.html")
   
  

  # checking authentication using admin username and password

def perform_login(request):
    if request.method != "POST":  
        return HttpResponse("Method is wrong")
    else:
        username=request.POST.get("username")  
        password=request.POST.get("password") 
        user_obj=authenticate(request,username=username, password=password)
        if user_obj is not None:
            login(request,user_obj)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            return HttpResponseRedirect("/")


def admin_dashboard(requst):
    return render(requst ,"admin_dashboard.html ")

# creating method for displaying details in html page
def food_details(request):
  mydata = FOODITEMS.objects.all()
  return render(request,"admin_dashboard.html",{'mydata':mydata})
 
 
def perform_logout(request):
    logout(request)  
    return render(request,"details.html")


    











