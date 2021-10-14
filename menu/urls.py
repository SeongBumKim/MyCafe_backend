from django.urls import path

from menu import views

urlpatterns = [
    path('', views.menu_list, name="menu_list"),
    path('<str:catagory>', views.menu_catagory_list, name="menu_catagory_list"),
    
    path('<int:pk>/', views.menu_detail, name="menu_detail"),
]