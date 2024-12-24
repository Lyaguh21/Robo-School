from django.urls import path
from . import views
from django.contrib import admin
from blog.views import registration

urlpatterns = [
	path('', views.main, name='main'),
	path('registr/', views.registration, name='registr'),
    path('authorization/', views.authorization, name='authorization'),
    path('admin/', admin.site.urls), 
]