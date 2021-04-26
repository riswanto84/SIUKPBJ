from django.urls import path
from . import views

urlpatterns = [
    # path untuk login admin
    path('administrator/', views.login_page, name='administrator'),
    # path untuk logout
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.accountSettings, name='account'),

    # path home admin
    path('home/', views.homeadmin, name='homeadmin'),

    # path untuk admin pengumuman
    path('admin_pengumuman/', views.admin_pengumuman, name='admin_pengumuman'),
    path('lampirkan_file/<str:pengumuman_id>/',
         views.lampirkan_file, name='admin_lampirkan_file'),
    path('delete_pengumuman/<str:pk>',
         views.delete_pengumuman, name='delete_pengumuman'),
    path('ubah_pengumuman/<str:pk>',
         views.ubah_pengumuman, name='ubah_pengumuman'),

    # path untuk admin berita
    path('admin_berita/', views.admin_berita, name='admin_berita'),
    path('lampirkan_file_berita/<str:berita_id>/',
         views.lampirkan_file_berita, name='lampirkan_file_berita'),
    path('delete_berita/<str:pk>',
         views.delete_berita, name='delete_berita'),
    path('ubah_berita/<str:pk>',
         views.ubah_berita, name='ubah_berita'),

    # path untuk tautan_aplikasi
    path('tautan_aplikasi/', views.tautan_aplikasi, name='tautan_aplikasi'),
    path('delete_tautan/<str:pk>',
         views.delete_tautan, name='delete_tautan'),
    path('ubahtautan/<str:pk>', views.ubah_tautan, name='ubahtautan'),

    # path untuk probis dan SOP
    path('admin_probis_sop/', views.admin_probis_sop, name='admin_probis_sop'),
]
