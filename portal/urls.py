from django.urls import path
from . import views

urlpatterns = [ 
     path('', views.home, name="home"),
     path('detail/<int:detil_id>/', views.detil_pengumuman, name='detil_pengumuman')
]