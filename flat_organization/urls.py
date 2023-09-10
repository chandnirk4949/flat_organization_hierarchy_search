# provide urls here
from django.urls import path

from . import views

urlpatterns = [
    path('search_employee/', views.search_employee, name='search_employee'),
]
