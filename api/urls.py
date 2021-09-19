from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_redirect),
    path('docs', views.documentation, name='docs'),
    path('titanic', views.TitanicAPI.as_view())
]
