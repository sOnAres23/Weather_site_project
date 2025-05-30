from django.urls import path
from . import views
from .api import city_autocomplete

urlpatterns = [
    path('', views.weather_view, name='weather'),
    path('history/', views.history_view, name='history'),
    path('api/city-autocomplete/', city_autocomplete, name='city_autocomplete'),
    path('api/stats/', views.api_city_search_stats, name='city_search_stats'),
]
