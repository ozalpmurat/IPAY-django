from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ip
from .models import birim

# İletişim formu paketi
from django import forms
class CommentForm(forms.Form):
    isim = forms.CharField(initial='hede hödö')
    url = forms.URLField()
    mesaj  = forms.CharField()
f = CommentForm(initial={'isim': 'İsminizi giriniz'}, auto_id=False)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ip_liste(request):
    ipler = ip.objects.all().order_by('eposta')
    birimler = birim.objects.all()
    return render(request, 'ip_list.html', {'ipler': ipler,'birimler' : birimler,'form':f})
