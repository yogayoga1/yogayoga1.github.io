from django.shortcuts import render, redirect
from .models import Surah, Kategori


def dashboard(request):
    template_name = 'back/base.html'
    context = {
        'title':'halaman dashboard',
    }
    return render(request, template_name, context)

def pengajian(request):
    template_name = 'back/tabel_pengajian.html'
    context = {
        'title':'halaman pengajian',
    }
    return render(request, template_name, context)

def surah(request):
    template_name = 'back/surah.html'
    surah = Surah.objects.all()
    context = {
        'title':'halaman surah',
        'surah' : surah
    }
    return render(request, template_name, context)

def tambah_surah(request):
    template_name = "back/tambah_surah.html"
    kategory = Kategori.objects.all()
    print(kategory)
    if request.method == "POST":
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kategory = request.POST.get('kategory')

        #panggil kategori
        kat = Kategori.objects.get(nama=kategory)
        Surah.objects.create(
            nama = nama,
            judul = judul,
            body = body,
            kategory=kat,
        )
        return redirect(surah)
    context = {
        'title': 'tambah surah',
        'kategory':kategory,
    }
    return render(request, template_name, context)

def lihat_surah(request, id):
    template_name = "back/lihat_surah.html"
    surah = Surah.objects.get(id=id)
    context = {
        'title':'lihat surah',
        'surah': surah,
    }
    return render(request, template_name, context)

def edit_surah(request, id):
    template_name = "back/edit_surah.html"
    s = Surah.objects.get(id=id)
    if request.method == "POST":
        judul = request.POST.get("judul")
        body = request.POST.get("body")
        #simpan data
        s.judul = judul
        s.body = body
        s.save()
        return redirect(surah)

    context = {
        'title':'edit surah',
        'surah': s,
    }
    return render(request, template_name, context)

def delete_surah(request, id):
    Surah.objects.get(id=id).delete()
    return redirect(surah)

