from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.  
#porduct_Id

def product_list(request):
    data = ['laptop','Mouse','Keyboard']

    dict = {'data':data}
    return JsonResponse(dict)

#Product_Detail

def product_detail(request,product_id):
    detail = f"""<h1> 'This is the details of product....{product_id}</h1>"""

    return HttpResponse(detail)