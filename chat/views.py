from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chat/index.html', {})


@login_required(login_url='chat:login')
def room(request, room_name):

    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
    })


def logoutUser(request):
    logout(request)
    return redirect('chat:index')


def loginUser(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # creates session
                return redirect('chat:index')
            else:
                messages.add_message(
                    request,  'Username or password is not correct')
        except:
            messages.add_message(
                request, messages.INFO, 'Username or password is not correct')
    return render(request, 'chat/login_register.html', {'page': page})


@login_required(login_url='chat:login')
def createRoom(request):
    page = "create"
    if request.method == "POST":
        room_name = request.POST['room_name']
        return redirect('chat:room', room_name)
    return render(request, 'chat/create_room.html', {'page': page})


@login_required(login_url='chat:login')
def joinRoom(request):
    page = "join"
    if request.method == "POST":
        room_name = request.POST['room_name']
        return redirect('chat:room', room_name)
    return render(request, 'chat/create_room.html', {'page': page})


def registerUser(request):
    page = "register"
    if request.method == "POST":
        try:
            if User.objects.get(username=request.POST["username"]):
                messages.add_message(
                    request, messages.INFO, 'Username already exist')
        except:
            user = User.objects.create(
                username=request.POST["username"],
                password=request.POST["password"]
            )
            login(request, user)
            return redirect('chat:index')
    return render(request, 'chat/login_register.html', {'page': page})
