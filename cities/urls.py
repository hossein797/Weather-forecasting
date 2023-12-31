from django.urls import path
from . import views

app_name = "cities"
urlpatterns = [
    path('', views.cities_list, name='cities'),
    path('<int:location_id>/', views.forecasts, name='forecast'),
]
