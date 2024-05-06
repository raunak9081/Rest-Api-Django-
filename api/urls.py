from django.urls import path
from .views import MyApiView


urlpatterns = [
    path('api/',  MyApiView.as_view(), name='MyApiView'),
    path('api/<int:id>/',  MyApiView.as_view(),name='apiview'),
    
    # Add other URL patterns as needed
]