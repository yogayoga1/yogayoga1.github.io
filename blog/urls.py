from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('surah/',surah, name='surah'),
    path('surah/tambah/', tambah_surah, name='tambah_surah'),
    path('surah/lihat/<str:id>', lihat_surah, name='lihat_surah'),
    path('surah/edit/surah/<str:id>', edit_surah, name='edit_surah'),
    path('surah/delete/surah/<str:id>', delete_surah, name='delete_surah'),
]