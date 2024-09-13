from django.shortcuts import render
from .models import Room, Message

def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')

    username = request.COOKIES.get('username', 'Anonymous')
    
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': username,
        'messages': messages
    })
