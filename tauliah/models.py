from django.db import models

# Create your models here.


class TP(models.Model):
    cawangan = models.TextField('Cawangan',blank=True,null=True,default="TB")
    kelas = models.TextField('Kelas Latihan',blank=True,null=True,default="TB")
    nama = models.TextField('Nama',blank=True,null=True,default="TB")
    noKP = models.TextField('noKP',blank=True,null=True,default="TB")
    status = models.TextField('Status',blank=True,null=True,default="TB")
    penyelia = models.TextField('Nama Penyelia',blank=True,null=True,default="TB")

    def __str__(self):
        return str(self.nama) +" - "+ str(self.kelas)
