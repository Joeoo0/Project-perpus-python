from django.shortcuts import render

def buku(request):
    judul = ["Belajar Django", "Belajar Python", "Belajar Bootstrap"]
    penulis = "Joeooo"

    konteks = {
        'title' : judul,
        'penulis' : penulis,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return ('Hallo Penerbit')
