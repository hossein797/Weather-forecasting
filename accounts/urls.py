from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('change_password/', views.change_password, name='change_password'),

]
