from django.shortcuts import render, redirect
from MeetUp.chat import *
from MeetUp.models import Current_Active_Users
# Create your views here.
def home(request):
    if request.method=='POST':
        selected_topic=request.POST['button']
        temp_username=request.POST['username']
        Current_Active_Users.objects.create(username=str(temp_username),selected_topic=str(selected_topic))
        return redirect('active_users',topic=str(selected_topic),current=str(temp_username))
        #except Exception as e:
        #   print(e)
        ##  return render(request,'home.html')
    return render(request,'home.html')
def active_users_on_topic(request,topic,current):
    if request.method=='POST':
        other_un=request.POST['other']
        main_un=request.POST['user']
    users=Current_Active_Users.objects.filter(selected_topic=str(topic))
    available_users=[]
    for user in users:
        if user.username!=current:
            available_users.append(user.username)
    return render(request,'current_active.html',{'users':available_users,'current':current})