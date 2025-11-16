
from django.contrib import admin
from django.urls import path , include

#Project Urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/',include('orders.urls')),
    path('product/',include('product.urls')),
    path('customer/',include('customer.urls'))
]
