from django.shortcuts import render
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
    return  render(request,'song.html',data)
