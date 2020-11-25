"""termin_app_projekt URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from termin_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('', login_required(views.CalendarView.as_view()), name="calendar"),
    url(r'^appointment/new/$', login_required(views.appointment), name='appointment_new'),
    url(r'^appointment/edit/(?P<appointment_id>\d+)/$', login_required(views.appointment), name='appointment_edit'),
]
