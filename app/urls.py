from django.urls import path
from .views import *

urlpatterns =[
    path('home/', home, name='home'),
    path('post/<uuid>/', post, name='post'),
    path('create_post/', create_post, name='create_post'),
    path('edit/<uuid>', edit, name='edit'),
    path('delete/<uuid>', delete, name='delete'),

]