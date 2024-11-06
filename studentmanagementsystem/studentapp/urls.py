from django.urls import path

from .views import *
urlpatterns=[
    path('',homepage,name='homepage'),
    path('aboutpage',aboutpage,name='aboutpage'),
    path('skillspage',skillspage,name='skillspage'),
    path('projectpage',projectpage,name='projectpage'),
    path('contactpage',contactpage,name='contactpage'),
]