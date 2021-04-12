from django.urls import path
from . import views

urlpatterns = [ 
     path('', views.home, name="home"),
     
     # path untuk pengumuman
     path('detail/<int:detil_id>/', views.detil_pengumuman, name='detil_pengumuman'),
     path('pengumuman/', views.all_pengumuman, name='pengumuman'),
     
     # path untuk berita
     path('detailberita/<int:detil_id>/', views.detil_berita, name='detil_berita'),
     path('berita/', views.all_berita, name='berita'),

     #path untuk visi dan misi
     path('visimisi/', views.visi_misi, name='visi_misi'),
]