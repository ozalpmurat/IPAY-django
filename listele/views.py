from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ip

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ip_liste(request):
    ipler = ip.objects.all().order_by('eposta')
    return render(request, 'ip_list.html', {'ipler': ipler})
