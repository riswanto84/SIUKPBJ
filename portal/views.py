from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):

    banners = Banner.objects.all()
    pengumuman = Pengumuman.objects.order_by('-id')[:3]
    berita = Berita.objects.order_by('-id')[:3]
    beritafooter = Berita.objects.order_by('-id')[:5]

    # query link aplikasi pada footer
    link_app1 = LinkApp.objects.all().order_by('id')[:6]
    link_app2 = LinkApp.objects.all().order_by('id')[6:10]

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


def tugas_kewenangan(request):
    tugas = TugasUKPBJ.objects.all()
    kewenangan = KewenanganUKPBJ.objects.all()
    context = {
        'tugas': tugas,
        'kewenangan': kewenangan,
    }

    return render(request, 'portal/tugas_kewenangan.html', context)


def struktur_organisasi(request):
    gambarstrukturOrganisasi = StrukturOrganisasi.objects.all()
    context = {
        'gambarstrukturOrganisasi': gambarstrukturOrganisasi,
    }

    return render(request, 'portal/struktur_organisasi.html', context)


def probis_sop(request):
    prosesbisnis = Probis.objects.all()
    context = {
        'prosesbisnis': prosesbisnis,
    }
    return render(request, 'portal/probis_sop.html', context)


def standar_dokumen(request):
    standar_dokumen = StandarDokumen.objects.all()
    context = {
        'standar_dokumen': standar_dokumen,
    }
    return render(request, 'portal/standar_dokumen.html', context)


def regulasi(request):
    regulasi = Regulasi.objects.all().order_by(
        '-id')  # Product.objects.all().order_by('id')
    context = {
        'regulasi': regulasi,
    }
    return render(request, 'portal/regulasi.html', context)


def materi(request):
    konten_materi = Materi.objects.all()
    context = {
        'materi': konten_materi,
    }
    return render(request, 'portal/materi.html', context)


def hubungi(request):
    context = {

    }
    return render(request, 'portal/hubungi.html', context)
