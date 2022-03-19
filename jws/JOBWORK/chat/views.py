from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home_chat.html')

def room(request, room):
    print('=-----------------------------------------')
    print(room)
    print('=-----------------------------------------')
    username = request.GET.get('username')
    #if any one of this is found
    try:
        room_details = Room.objects.get(name=room)
    except:
        #split
        splitroom = room.split('-')

        room = '-'.join([splitroom[1],splitroom[0]])


        try:
            room_details = Room.objects.get(name=room)
            #create new room and add it to db
        except:
             new_room = Room.objects.create(name=room)
             new_room.save()
             room_details = Room.objects.get(name=room)
    # try:
    #  room_details = Room.objects.get(name=room)
    
    # except:
    #     names=room.split('-')
    #     try:
    #         room_details = Room.objects.get(name=f'{names[1]}-{names[0]}')
    #         return render(request, 'room.html', {
    #             'username': username,
    #             'room': room,
    #             'room_details': room_details
    #         })


    #     except:
    #         pass
    #     new_room = Room.objects.create(name=room)
    #     new_room.save()
    #     room_details = Room.objects.get(name=room)


        
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):

    #to do chaek for session on uname
    room = request.POST['room_name']
    username =  request.session.get('uname')

    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.session.get('uname')
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})