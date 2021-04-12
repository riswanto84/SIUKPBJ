from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):

    banners = Banner.objects.all()
    pengumuman = Pengumuman.objects.order_by('-id')[:3]
    berita = Berita.objects.order_by('-id')[:3]
    beritafooter = Berita.objects.order_by('-id')[:5]
    link_app1 = LinkApp.objects.all().order_by('-id')[:6]
    link_app2 = LinkApp.objects.order_by('id')[6:10]

    context = {
        'banners': banners,
        'pengumuman': pengumuman,
        'berita': berita,
        'beritafooter': beritafooter,
        'link_app1': link_app1,
        'link_app2': link_app2,
    }
    return render(request, 'portal/portal_index.html', context)


def detil_pengumuman(request, detil_id):
    detil_pengumuman = Pengumuman.objects.get(id=detil_id)
    files = PengumumanFile.objects.filter(pengumuman_id=detil_id)

    context = {
        'detil_pengumuman': detil_pengumuman,
        'files': files,
    }
    return render(request, 'portal/detil_pengumuman.html', context)

def all_pengumuman(request):
    pengumuman = Pengumuman.objects.all().order_by('-id')
    context = {
        'pengumuman': pengumuman,
        'halaman': " / semua pengumuman",
    }
    return render(request, 'portal/pengumuman.html', context)

def detil_berita(request, detil_id):
    detil_berita = Berita.objects.get(id=detil_id)
    files = BeritaFile.objects.filter(berita_id=detil_id)

    context = {
        'detil_berita': detil_berita,
        'files': files,
    }
    return render(request, 'portal/detil_berita.html', context)

def all_berita(request):
    berita = Berita.objects.all().order_by('-id')
    context = {
        'berita': berita,
        'halaman': " / semua berita",
    }
    return render(request, 'portal/berita.html', context)
    
def visi_misi(request):
    visi = Visi.objects.all()
    misi = Misi.objects.all()
    context = {
        'visi': visi,
        'misi': misi,
    }

    return render(request, 'portal/visimisi.html', context)