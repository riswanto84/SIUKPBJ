from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal.models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from django.forms import modelformset_factory, inlineformset_factory
from django.core.files.storage import FileSystemStorage
from crispy_forms.helper import FormHelper

# Create your views here.


@login_required(login_url='administrator')
def accountSettings(request):
    user = request.user.useradmin
    form = UserAdminForm(instance=user)
    # print(form)

    if request.method == 'POST':
        form = UserAdminForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            messages.info(request, 'Data berhasil diubah')

    context = {'form': form}
    return render(request, 'adminportal/account_settings.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeadmin')
        else:
            messages.info(request, 'Username atau Password tidak valid!')

    context = {}
    return render(request, 'adminportal/loginpage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('administrator')


@login_required(login_url='administrator')
def homeadmin(request):
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


@login_required(login_url='administrator')
def pengumuman(request):
    context = {

    }
    return render(request, 'adminportal/pengumuman.html', context)


@login_required(login_url='administrator')
def admin_pengumuman(request):

    pengumuman = Pengumuman.objects.all().order_by('-id')
    form = PengumumanForm()

    if request.method == 'POST':
        form = PengumumanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_pengumuman')

    context = {
        'pengumuman': pengumuman,
        'form': form,
    }
    return render(request, 'adminportal/admin_pengumuman.html', context)


@login_required(login_url='administrator')
def lampirkan_file(request, pengumuman_id):
    pengumuman = Pengumuman.objects.get(id=pengumuman_id)
    LampiranPengumumanFormset = inlineformset_factory(
        Pengumuman, PengumumanFile, fields=('files',), can_delete=False, extra=3)

    if request.method == 'POST':
        formset = LampiranPengumumanFormset(
            request.POST, request.FILES, instance=pengumuman)
        if formset.is_valid():
            formset.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_pengumuman')

    formset = LampiranPengumumanFormset(instance=pengumuman)

    return render(request, 'adminportal/lampirkan_file.html', {'formset': formset})


@login_required(login_url='administrator')
def delete_pengumuman(request, pk):
    pengumuman = Pengumuman.objects.get(id=pk)
    pengumuman.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('admin_pengumuman')


@login_required(login_url='administrator')
def ubah_pengumuman(request, pk):
    pengumuman = Pengumuman.objects.get(id=pk)
    form = PengumumanForm(instance=pengumuman)

    if request.method == 'POST':
        form = PengumumanForm(request.POST, request.FILES, instance=pengumuman)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_pengumuman')

    context = {'form': form}
    return render(request, 'adminportal/admin_ubahpengumuman.html', context)
