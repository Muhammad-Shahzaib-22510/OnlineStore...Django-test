from django.urls import path 
from product import views

#Project Urls

urlpatterns = [
      path('',views.product_list),
    path('<int:product_id>',views.product_detail)
    ]