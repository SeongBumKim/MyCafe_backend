from django.urls import path

from menu import views

urlpatterns = [
    path('', views.menu_list, name="menu_list"),
    path('<int:pk>/', views.menu_detail, name="menu_detail"),
    path('<str:ca>/', views.menu_category_list, name="menu_category_list"),
]