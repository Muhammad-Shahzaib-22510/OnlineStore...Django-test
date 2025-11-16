from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.

def profile(request):
    customer_profile= {
        'name': 'shakeel',
        'email': "shakeel@gmail.com"
    }
    
    return JsonResponse(customer_profile)

def dashboard(request):
    customer_dashboard = """ 
    <h1 style='color:violet' font-size:40px>This is customer Dashboard......</h1>
    """

    return HttpResponse(customer_dashboard)  