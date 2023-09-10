from django.shortcuts import render, redirect
from app1.models import Song, Artist
# Create your views here.
def main_url(request):
    """Main url"""
    data_base = {
        'count_song': len(Song.objects.all()),
        'count_artist': len(Artist.objects.all())
    }
    return render(request, 'index.html', data_base)

def song_url(request):
    """Song URL"""
    data = {
        'data_song': Song.objects.all()
    }
    return  render(request, 'song.html', data)

def song_url2(request, id):
    """Songni ustiga bosgandagi holatlar"""
    data_url = Song.objects.get(id=id)

    return render(request, 'song_about.html', {'Song': data_url})

def artist_url(request):
    data = {
        'data_artist': Artist.objects.all()

    }

    return render(request, 'artist.html', data)

def success(request):

    return render(request, 'success.html')

def delete(request, id):


    delete =  Song.objects.get(id=id).delete()



    return redirect('http://127.0.0.1:8000/home/success/')

def delete_a(request, id):

    delete = Artist.objects.get(id=id).delete()

    return redirect('http://127.0.0.1:8000/home/success/')


def artist_url2(request, id):
    data_url = Artist.objects.get(id=id)

    return render(request, 'artist_about.html', {'Artist': data_url})