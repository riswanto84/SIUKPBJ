from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    
    banners = Banner.objects.all()
    pengumuman = Pengumuman.objects.order_by('-id')[:3]

    context = {
        'banners': banners,
        'pengumuman': pengumuman,
        }
    return render(request, 'portal/portal_index.html', context)

def detil_pengumuman(request, detil_id):
    detil_pengumuman = Pengumuman.objects.get(id=detil_id)
    context = {
        'detil_pengumuman': detil_pengumuman,
        'halaman': "Beranda / pengumuman / detail pengumuman",
    }
    return render(request, 'portal/detil_pengumuman.html', context) 
