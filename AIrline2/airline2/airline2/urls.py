"""airline2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from airline_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.signup),
    path('',views.signin),
    path('logout',views.signout),
    path('view_form',views.view_form),
    path('view_data',views.view_data),
    path('flight',views.flight),
    path('reservation/<int:id>',views.reservation),
    path('delete/<int:id>',views.delete_data),
    path('views',views.view_data),
    path('update/<int:id>',views.update_data),
    path('home',views.home),
    path('re',views.re),
    path('contact',views.contact),
    path('ticket',views.ticket),
]
