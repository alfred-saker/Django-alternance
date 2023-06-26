from django.urls import path
from alternance import views

urlpatterns = [
    
    path('',views.home_view, name="home"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('add/', views.add_view, name="add"),
]

