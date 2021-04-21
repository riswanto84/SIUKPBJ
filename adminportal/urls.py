from django.urls import path
from . import views

urlpatterns = [
    # path untuk login admin
    path('administrator/', views.login_page, name='administrator'),
    # path untuk logout
    path('logout/', views.logoutUser, name='logout'),

    # path home admin
    path('home/', views.home, name='home'),

    # path pengumuman admin
    path('admin_pengumuman/', views.admin_pengumuman, name='admin_pengumuman'),
]
