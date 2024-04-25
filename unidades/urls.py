from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('cadastro_filial/', views.cadastro_filial, name="cadastro_filial"),
]