from django.forms import ModelForm
from portal.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class PengumumanForm(ModelForm):
    class Meta:
        model = Pengumuman
        fields = ['title', 'description', 'image', 'created_by']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'created_by': forms.HiddenInput(),
        }

        labels = {
            'title': _('Judul'),
            'description': _('Isi Pengumuman'),
            'image': _('File gambar'),
        }
