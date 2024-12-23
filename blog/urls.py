from django.urls import path
from . import views
urlpatterns = [
	path('', views.main, name='main'),
	path('registration/', views.registrarion, name='registration'),
    path('authorization/', views.authorization, name='authorization'),
    
]