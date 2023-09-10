"""
URL configuration for Song project.

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
from app1.views import main_url, song_url, song_url2, delete, artist_url, success, artist_url2, delete_a
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_url),
    path('song/', song_url),
    path('song_about/<int:id>/', song_url2),
    path('artist/', artist_url),
    path('delete/<int:id>/', delete),
    path('home/success/', success),
    path('artist_about/<int:id>/', artist_url2),
    path('delete_a/<int:id>/', delete_a)

]


