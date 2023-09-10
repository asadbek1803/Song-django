from django.shortcuts import render, redirect
from app1.models import Song
# Create your views here.
def main_url(request):
    """Main url"""

    return render(request, 'index.html')

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


def delete(request, id):


    delete =  Song.objects.get(id=id).delete()



    return redirect('http://127.0.0.1:8000/song/')


