from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm, MeetingForm
from .models import Genre, Message, User, Game, Meeting
from django.contrib import messages
from dateutil.relativedelta import relativedelta


def landing_page(request):

    q = request.GET.get('q') if request.GET.get('q') != None else '' #q is what was passed into the url
    meetings = Meeting.objects.filter(
        Q(game__genre__name__icontains=q) |  
        Q(game__name__icontains=q) | 
        Q(name__icontains=q) | 
        Q(description__icontains=q) ) #from rooms filters to topic and then to name and icontains checks if it contains some letters from q

    genres = Genre.objects.all()
    games = Game.objects.all()
    meeting_count = genres.count() #length of a query set faster than len
    #room_messages = Message.objects.filter(Q(room__topic__name__icontains=q)) #the name of the topic of the selected room #CHANGE THIS TO HAVE ONLY PEOPLE YOU FOLLOW

    context = {'meetings' : meetings, 'genres' : genres, 'meeting_count' : meeting_count,'games':games}
    
    return render(request,'landing_page.html',context)

def login_user(request):
    page = 'login'
    if request.user.is_authenticated: #makes sure a user can't log in twice
        return redirect('landing_page')

    if request.method == 'POST':
        username = request.POST.get('username').lower() #gets the username from the POST method
        password = request.POST.get('password') #gets the password from the POST method

        try:
            user = User.objects.get(username = username) #checks if username = username
        except:
            messages.error(request, 'User does not exist') #LOOK UP FLASH MEESAGES

        user = authenticate(request, username=username, password=password) #authenticates the user after checking for errors above

        if user is not None: #if a user 
            login(request, user) #login the user
            return redirect('landing_page')

        else:
            messages.error(request, "Username or password does not exist")

    context = {'page': page}
    return render(request,'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('landing_page')

def register_user(request):
    page = 'register'
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #allows to get user before commiting
            #CLEAN DATA
            user.username = user.username.lower()
            user.save()
            login(request,user) #logs user in
            print("user created")
            return redirect('landing_page')
        else:
            messages.error(request, 'An error has ocurred during registration')

    return render(request, 'login.html',{'form':form})

@login_required(login_url='login')
def createMeeting(request):

    form = MeetingForm()
    games = Game.objects.all()
    if request.method == 'POST': #checks if post button has been pressed
        #game_name = request.POST.get('game') #topic is the name given in the html, will work for adding topics
        #game, created = Game.objects.get_or_create(name=game_name) #creates a topic if it cant find one
        if form.is_valid():
            form.save()
            print("saved")
            
            return redirect('landing_page')

    context = {f'form': form, 'games':games}
    return render(request, 'meeting_form.html' ,context)


