from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('titanic/', views.titanic_model, name="titanic-model")
]

