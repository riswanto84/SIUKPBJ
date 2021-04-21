from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal.models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username atau Password tidak valid!')

    context = {}
    return render(request, 'adminportal/loginpage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('administrator')


@login_required(login_url='administrator')
def home(request):
    tot_pengumuman = Pengumuman.objects.all().count()
    tot_berita = Berita.objects.all().count()
    tot_aplikasi = LinkApp.objects.all().count()
    tot_probisSOP = Probis.objects.all().count()
    tot_stdDokumen = StandarDokumen.objects.all().count()
    tot_regulasi = Regulasi.objects.all().count()
    tot_banner = Banner.objects.all().count()

    context = {
        'tot_pengumuman': tot_pengumuman,
        'tot_berita': tot_berita,
        'tot_aplikasi': tot_aplikasi,
        'tot_probisSOP': tot_probisSOP,
        'tot_stdDokumen': tot_stdDokumen,
        'tot_regulasi': tot_regulasi,
        'tot_banner': tot_banner,
    }
    return render(request, 'adminportal/dashboard.html', context)
