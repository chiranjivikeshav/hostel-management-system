from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Students.as_view()),
]