from django.urls import path 
from customer import views

#Project Urls

urlpatterns = [
    path('profile/',views.profile),
    path('dashboard',views.dashboard)
    
    ]