from django.urls import path
from .views import *

app_name='myapp1'

urlpatterns=[
    path('',home,name='home'),
    path('signin/',signin,name='signin'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
     path('callback/',callback,name='callback')
]
