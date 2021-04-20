from django.urls import path
from . import views

urlpatterns = [
    # path untuk login
    path('adminportal', views.login_page, name='adminportal'),
    # path untuk logout
    path('logout/', views.logoutUser, name='logout'),

    # path home admin
    path('home', views.home, name='home')
]
