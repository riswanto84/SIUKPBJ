from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # path untuk pengumuman
    path('detail/<int:detil_id>/', views.detil_pengumuman, name='detil_pengumuman'),
    path('pengumuman/', views.all_pengumuman, name='pengumuman'),

    # path untuk berita
    path('detailberita/<int:detil_id>/',
         views.detil_berita, name='detil_berita'),
    path('berita/', views.all_berita, name='berita'),

    # path untuk visi dan misi
    path('visimisi/', views.visi_misi, name='visi_misi'),

    # path untuk tugas dan fungsi
    path('tugaskewenangan/', views.tugas_kewenangan, name='tugas_kewenangan'),

    # path untuk struktur organisasi
    path('strukturorganisasi/', views.struktur_organisasi,
         name='struktur_organisasi'),

    # path untuk probis dan SOP
    path('probis_sop/', views.probis_sop, name='probis_sop'),

    # path untuk standar dokumen
    path('standardokumen/', views.standar_dokumen, name='standar_dokumen'),

    # path untuk regulasi
    path('regulasi/', views.regulasi, name='regulasi'),

    # path untuk hubungi kami
    path('kontak/', views.hubungi, name='kontak'),


]
