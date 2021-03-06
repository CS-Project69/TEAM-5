"""CEWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
'''from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]'''

from django.contrib import admin
from django.urls import path
from addNew import views
from panverify import views as panviews
from creditv import views as creditviews
from emailv import views as emailviews
from contactus import views as contactviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('call/',views.call,name='call'),
    path('about/',views.about,name='about'),
    path('aadhar/',views.aadhar,name='aadhar'),
    path('panv/',panviews.panv,name='panv'),
    path('creditv/',creditviews.creditv,name='creditv'),
    path('valid/',creditviews.valid,name='valid'),
    path('emailv/',emailviews.emailv,name='emailv'),
    path('contact/',contactviews.contact,name='contact')
]
