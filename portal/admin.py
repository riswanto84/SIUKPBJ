from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Banner)
admin.site.register(Pengumuman)
admin.site.register(PengumumanFile)
admin.site.register(Berita)
admin.site.register(BeritaFile)
admin.site.register(LinkApp)
admin.site.register(Visi)
admin.site.register(Misi)
