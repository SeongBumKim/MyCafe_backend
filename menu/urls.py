from django.urls import path

from menu import views

urlpatterns = [
    path('', views.menu_list, name="menu_list"),
    path('detail/<int:pk>/', views.menu_detail, name="menu_detail"),
    path('category/<str:ca>/', views.menu_category_list, name="menu_category_list"),
    path('order/', views.order_list, name="order_list"),
    path('order/<int:pk>', views.ordered_menu, name="ordered_menu"),
    path('create/', views.order_create, name="order_create"),
]