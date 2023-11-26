"""
URL configuration for pharmacy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view),
    path('controlpage',views.controlpage),
    path('home',views.home),
    path('loginform',views.loginform),
    path('logout',views.logout),
    path('addmedicine',views.addmedicine),
    path('deletemedicine/<int:id>', views.deletemedicine, name='deletemedicine'),
    path('editmedicine/<int:id>', views.editmedicine, name='editmedicine'),
    path('addsalesview',views.addsalesview),
    path('addsales',views.addsales),
    path('deletesales/<int:id>', views.deletesales, name='deletesales'),

]





