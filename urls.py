from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_crop, name='predict_crop'),
]


