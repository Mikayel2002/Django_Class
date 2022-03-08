from django.urls import path
from homework_2 import views

urlpatterns = [
    path('hello/', views.hello)
]
