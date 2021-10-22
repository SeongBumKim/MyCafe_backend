from django.urls import path

from login import views

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('users/', views.user_list, name="user_list")
]