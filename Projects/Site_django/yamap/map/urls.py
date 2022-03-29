from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cat/<int:catid>/', category),
    path('about', about, name='about')
]