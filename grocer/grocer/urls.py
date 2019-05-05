"""grocer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from testapp.views import DemoView, HomeView, DemoDash, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', DemoView.as_view()),
    path('demo/signup/', SignupView.as_view()),
    path('demo/account/', DemoDash.as_view()),
    path('', HomeView.as_view())
]
