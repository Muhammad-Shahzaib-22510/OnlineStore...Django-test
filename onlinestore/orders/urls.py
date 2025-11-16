from django.urls import path
from orders import views

urlpatterns = [
    path('place/',views.place_order),
    path('history',views.order_history)
]
