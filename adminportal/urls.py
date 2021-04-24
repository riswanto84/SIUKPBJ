from django.urls import path
from . import views

urlpatterns = [
    # path untuk login admin
    path('administrator/', views.login_page, name='administrator'),
    # path untuk logout
    path('logout/', views.logoutUser, name='logout'),

    # path home admin
    path('home/', views.homeadmin, name='homeadmin'),

    # path pengumuman admin
    path('admin_pengumuman/', views.admin_pengumuman, name='admin_pengumuman'),
    path('lampirkan_file/<str:pengumuman_id>/',
         views.lampirkan_file, name='admin_lampirkan_file'),
    path('delete_pengumuman/<str:pk>',
         views.delete_pengumuman, name='delete_pengumuman'),
    path('ubah_pengumuman/<str:pk>',
         views.ubah_pengumuman, name='ubah_pengumuman'),

]
