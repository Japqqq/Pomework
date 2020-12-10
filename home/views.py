from django.shortcuts import render , redirect
from home.models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from home.forms import CreateUserform
from home.decorations import unauthenticated_user , allowed_users , admin_only

from django.contrib.auth.decorators import login_required
from home.forms import *





@login_required(login_url='loginPage')

def index(request):
    playlist = Playlist.objects.all()
    context = {'playlist' : playlist}
    if request.user.is_superuser:
        
        return redirect('adminpage')
    

    return render(request , 'home.html' , context)
@login_required(login_url='loginPage')
def Favor(request , pk):
    account = Account.objects.get(id = pk)
    items = account.playlist_set.all()
    playlist = Playlist.objects.all()
    context = { 'account' : account , 'items' : items}
    return render(request , 'Favor.html' , context)

@login_required(login_url='loginPage')
def UpdateFavor(request ,ak , pk):
    account = Account.objects.get(id = ak)
    item = get_object_or_404(Playlist , id=pk)
    account.playlist_set.add(item)

  

       
    return redirect('/')
@login_required(login_url='loginPage')
def RemoveFavor(request ,ak, pk):
    account = Account.objects.get(id = ak)
    item = get_object_or_404(Playlist , id=pk)
    account.playlist_set.remove(item)
   

    return redirect('/') 
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

@unauthenticated_user
def register(request):
    form = CreateUserform()
    
    if request.method == "POST":
         form = CreateUserform(request.POST)
         if form.is_valid():
             user = form.save()
             username = form.cleaned_data.get('username')
             Account.objects.create(user = user,)
             return redirect('loginPage')
    context = {
        'form' : form
        
    }
        

    return render(request ,'register.html' , context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request , username=username, password = password)
      
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}

    return render(request , 'login.html' , context)
def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def about(request):
    return render(request , 'about.html')

@admin_only
def admin(request):
    playlist = Playlist.objects.all()
    context = {'playlist' : playlist}
    

    return render(request , 'admin.html' , context)

def ap(request):
    form = PlaylistForm()

    if request.method == "POST":
        form = PlaylistForm(request.POST , request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('adminpage')
    context = {
        'form' : form
    }

    return render(request , 'ap.html' , context)
@admin_only
def delete(request , pk):
    item = get_object_or_404(Playlist , id=pk)
    item.delete()
    return redirect('adminpage')

@login_required(login_url='loginPage')
def homework(request, pk):
    form = HomeworkForm()
    account = Account.objects.get(id = pk)
    items = account.todo_set.all()
    
    if request.method == "POST":
        form = HomeworkForm(request.POST , request.FILES)
        if form.is_valid():
            hm = form.save()
            account.todo_set.add(hm)
             
        
            
    
    context = { 'account' : account , 'items' : items , 'form' : form}
    return render(request , 'Homework.html' , context)
@login_required(login_url='loginPage')
def removehomework(request, ak, pk):
    accountme = Account.objects.get(id = ak)
    item = get_object_or_404(Todo , id=pk)
    accountme.todo_set.remove(item)
    items = accountme.todo_set.all()
    form = HomeworkForm()
    context = { 'accountme' : accountme , 'items' : items , 'form' : form}
    return render(request , 'Homework.html' , context)