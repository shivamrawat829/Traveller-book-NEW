from django.shortcuts import render

# Create your views here.
def res_home(request):
    return render(request,'google_login/home.html')