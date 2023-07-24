from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu-item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings, name='bookings'), 
    path('register/', views.register, name='register'), 
    path('login/',auth_views.LoginView.as_view(template_name='signin.html'),name='signin'),
    path('logout',auth_views.LogoutView.as_view(template_name='signout.html'),name='signout'),
]