from django.shortcuts import render , redirect
from home.models import Playlist
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    playlist = Playlist.objects.all()
    context = {'playlist' : playlist}
    

    return render(request , 'home.html' , context)

def Favor(request):
    playlist = Playlist.objects.all()
    context = {'playlist' : playlist }
    return render(request , 'Favor.html' , context)


def UpdateFavor(request , pk):
    item = get_object_or_404(Playlist , id=pk)
    item.fav = True
    item.save()
  

       
    return redirect('/')

def RemoveFavor(request , pk):
    item = get_object_or_404(Playlist , id=pk)
    item.fav = False
    item.save()

    return redirect('/Favor')
def search(request):
    search_query = request.GET.get('search' , '')
    if search_query:
        playlist = Playlist.objects.filter(description__icontains = search_query)
    else:
        playlist = Playlist.objects.all()
    
    context = {
        'playlist' : playlist
    }

    return render(request,'home.html' , context)
   

    
    
    