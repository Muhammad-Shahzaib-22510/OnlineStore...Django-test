from django.shortcuts import render
from django.http import HttpResponse , JsonResponse


# place order

def place_order(request):
    return HttpResponse('<h1>Order Placed successfully ....</h1>')

#order history
def order_history(request):
    orders =[
           {'id': '1','item': 'lapotop'},
           {'id': '2','item': 'mouse'}
    ]
    dict = {'orders':orders}
    return JsonResponse(dict)    
