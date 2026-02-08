from django.contrib import admin
from django.urls import path
from gisapp import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.login_page),
     path('home/', views.home_page, name='home'),
     path('external/', views.Myexternal, name='Suresh'),
]