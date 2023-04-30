"""ny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('bas/',views.bas,name="bas"),
    path('b/',views.b,name="b"),
    path('b/<int:id>/<str:name>',views.aa,name="a"),
    path('login/', views.login, name='login'),
    path('register/', views.register_view, name='register'),
    path('driverlogin/', views.driverlogin, name='driverlogin'),
    path('logout/', views.logout_view, name='logout'),
    path('holidays/',views.get_holidays, name='get_holidays'),
    path('submit_review/',views.submit_review, name='submit_review'),
    path('reviews/',views.view_reviews, name='reviews'),
    path('contactus/',views.c,name="c"),
    path('map',views.map_view,name="m"),
]

