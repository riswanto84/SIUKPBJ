from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Banner(models.Model):
    description = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Pengumuman(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PengumumanFile(models.Model):
    pengumuman = models.ForeignKey(Pengumuman, on_delete=models.CASCADE)
    files = models.FileField(
        max_length=255, upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.pengumuman.title


class Berita(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BeritaFile(models.Model):
    berita = models.ForeignKey(Berita, on_delete=models.CASCADE)
    files = models.FileField(
        max_length=255, upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.berita.title


class LinkApp(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    thumbnailImage = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title


class Visi(models.Model):
    visi = models.TextField()

    def __str__(self):
        return self.visi


class Misi(models.Model):
    misi = models.TextField()

    def __str__(self):
        return self.misi


class TugasUKPBJ(models.Model):
    tugas = models.TextField()

    def __str__(self):
        return self.tugas


class KewenanganUKPBJ(models.Model):
    kewenangan = models.TextField()

    def __str__(self):
        return self.kewenangan


class StrukturOrganisasi(models.Model):
    title = models.CharField(max_length=500)
    gambar = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title


class Probis(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    file = models.FileField(
        max_length=255, upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.title


class SOP(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    file = models.FileField(
        max_length=255, upload_to='files/', blank=True, null=True)
    probis = models.ForeignKey(
        Probis, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class StandarDokumen(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title


class SDF(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(
        max_length=255, upload_to='files/', blank=True, null=True)
    dokumen = models.ForeignKey(
        StandarDokumen, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.dokumen.title
