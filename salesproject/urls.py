"""salesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from salesrecord import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('', views.display_records, name='display_records'),
    path('edit/<int:id>/', views.edit_record, name='edit_record'),
    path('add', views.add_record, name='add_record'),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),
    path('download', views.export, name='download_record'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout')
]
