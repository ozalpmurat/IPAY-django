from django.urls import path
from . import views

app_name = 'listele'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.ip_liste, name='ip_liste'),
]
