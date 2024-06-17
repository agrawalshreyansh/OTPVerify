from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name="Login"),
    path('submit', views.submit, name="submit" )
]

