"""
URL configuration for NetworkConfigurationProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home_page"),
    path('add_network_config/', views.add_network_config, name='add_network_config'),
    path('edit_network_config/<int:config_number>/', views.edit_network_config, name='edit_network_config'),
    path('login/', views.custom_login, name='custom_login'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.custom_logout, name='logout'),
    path('change_approval_status/<int:config_number>/<str:status>/', views.change_approval_status, name='change_approval_status'),
]
