from django.urls import path

## I'm importing the views needed for the url
from .views import Home , NewCompany ,DeleteCompany , EditCompany

urlpatterns = [
    
    path('',Home,name='home'),
    path('newcompany',NewCompany,name='newcompany'),
    path('deletecompany/<int:pk>',DeleteCompany,name='deletecompany'),
    path('editcompany/<int:pk>',EditCompany,name='editcompany'),
]