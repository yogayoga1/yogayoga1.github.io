from django.contrib import admin
from django.urls import path, include
from alquranku.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('blog.urls')),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('pengajian', pengajian, name='pengajian'),
    path('contact', contact, name='contact'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
]