from django.forms import ModelForm
from portal.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class PengumumanForm(ModelForm):
    class Meta:
        model = Pengumuman
        fields = ['title', 'description', 'image', 'created_by']

        widgets = {
            'created_by': forms.HiddenInput(),
        }

        labels = {
            'title': _('Judul Pengumuman'),
            'description': _('Isi Pengumuman'),
            'image': _('File gambar'),
        }


class UserAdminForm(ModelForm):
    class Meta:
        model = UserAdmin
        fields = '__all__'
        exclude = ['user']

        labels = {
            'nama': _('Nama Lengkap'),
            'no_hp': _('Nomor HP'),
            'email': _('Alamat Email'),
            'profil_pic': _('Foto Profil'),

        }
