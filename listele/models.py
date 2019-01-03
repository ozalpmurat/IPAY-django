from django.db import models
from macaddress.fields import MACAddressField

class birim(models.Model):
    isim = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.isim)

class ip(models.Model):
    tarih = models.DateTimeField('date published')
    ip = models.GenericIPAddressField(db_index=True, primary_key=True)
    birim = models.ForeignKey(birim, on_delete=models.PROTECT)
    #eposta = models.EmailField(max_length=50)
    eposta = models.CharField(max_length=50)
    aciklama = models.CharField(max_length=250)
    mac = MACAddressField(blank=True, integer=False)
    kisisel = models.BooleanField(default=False)
    elle_binding = models.BooleanField(default=False)
    kablosuz = models.BooleanField(default=False)
    aktif = models.BooleanField(default=True)
    def publish(self):
        self.tarih = timezone.now()
        self.save()
    def detay(self):
        return '{} - {} - {} - {}'.format(self.ip, self.mac, self.eposta, self.birim)
    def __str__(self):
        return self.detay()
