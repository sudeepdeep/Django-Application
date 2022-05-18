from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.core.mail import send_mail
import datetime
from .models import CreateUser, TeamModel, CreateTask, TaskModels

lead_name = "sudeep"
member_name = "manoj"

def users(request):
    return render(request, 'users/index.html')

def createteam(request):
    team_members = []
    teamleaders  = CreateUser.objects.all()
    if request.method == 'POST':
        
        
        for i in teamleaders:
            if(i.role == "Team Member"):
                
                try:
                    teammembers = request.POST[f'{i.name}']
                    team_members.append(teammembers)  
                except:
                    print("nothing")

        form = forms.CreateNewTeam(request.POST) 
        if form.is_valid():
            teammod = TeamModel()
            teamname = form.cleaned_data['teamname']
            teamlead = request.POST['tl']
            print("this is lead data: ", teamlead, teamname)
            teammod.name = teamlead
            teammod.teamname = teamname
            teammod.role = 'Team Lead'
            teammod.save()

        for i in team_members:
            teammod = TeamModel()
            teammod.name = i
            teammod.teamname = teamname
            teammod.role = 'Team Member'
            teammod.save()

        msg = "Team Created Successfully"
        return render(request, 'users/index.html', {'msg': msg})

    else:
        teamleaders  = CreateUser.objects.all()
        form = forms.CreateNewTeam()
    return render(request, 'users/createteam.html', {'form': form, 'tl': teamleaders})



created_teams = []
def createtask(request):

    if request.method == 'POST':
        taskname = request.POST['taskname']
        teamname = request.POST['teamname']
        description = request.POST['desc']
        print(taskname, teamname, description)
        createtask = CreateTask()
        createtask.taskname = taskname
        createtask.team = teamname
        createtask.description = description
        createtask.save()

        emailmodel = TeamModel.objects.all()
        final_name = ""
        final_email = ""
        for i in emailmodel:
            if i.role == 'Team Lead' and i.teamname == teamname:
                final_name = i.name

        
        emailuser = CreateUser.objects.all()
        for j in emailuser:
            if j.name == final_name:
                final_email = j.email

        
        send_mail(
            'New Task Assigned',
            f'Hello {final_name}, A new Task Has been assigned to You. Please go and check.',
            'django0514@gmail.com',
            [final_email],
        )

        msg = "Task created successfully & mail has been sent successfully to the Team Lead"
        return render(request, 'users/index.html',{'msg': msg})

    else:

        teams = TeamModel.objects.all()
        for i in teams:
            if(i.teamname in created_teams):
                print("present")
            else:
                created_teams.append(i.teamname)

    

    
    return render(request, 'users/createtask.html', {'teams': created_teams})



def taskstolead(request):

    list_dic ={}
    list_mem = []
    dummy_team = ""
    assign_mems = []
    teamassign = CreateTask.objects.all()
    teams = TeamModel.objects.all()
    for i in teams:
        if(i.name == lead_name):
            list_dic['teamlead'] = i.name
            list_dic['teamname'] = i.teamname
            dummy_team = i.teamname

    for j in teams:
        if(j.teamname == dummy_team and j.role == "Team Member"):
            list_mem.append(j.name)
    
    for k in teamassign:
        print(k.team, dummy_team)
        if(k.team == dummy_team.split(' ')[0]):
            list_dic['taskname'] = k.taskname
            list_dic['description'] = k.description
    
    if(len(list_mem) > 0):
        list_dic['members'] = list_mem

    print("this is the final dic: ", list_dic)


    if(request.method == 'POST'):
        status = request.POST['status']

        for i in teams:
            try:
                if i.name == request.POST[f'{i.name}']:
                    if(i.name in assign_mems):
                        print("present")
                    else:
                        assign_mems.append(i.name)
            except:
                print("nothing")

        
        
        for i in assign_mems:
            taskmo = TaskModels()
            taskmo.name = i
            taskmo.team = dummy_team
            taskmo.status = status
            taskmo.task = list_dic['taskname']
            taskmo.taskdesc = list_dic['description']
            taskmo.save()
        msg = "Assigned successfully"
        return render(request, 'users/taskstolead.html', {'teams': list_dic, 'msg': msg})
    else:
        return render(request, 'users/taskstolead.html', {'teams': list_dic})




def tasktomember(request):
    
    gettasks = TaskModels.objects.all()
    return render(request, 'users/tasktomember.html', {'tasks': gettasks, 'username':member_name})

def updatestatus(request, task):
    if request.method == 'POST':
        ustatus = request.POST['status']

        gettasks = TaskModels.objects.all()

        for i in gettasks:
            print(i.task)
            if i.name == member_name and i.task == task:
                if(ustatus == "Done"):
                    current_datetime = datetime.datetime.now()  
                    i.completed = current_datetime
                    i.status = ustatus
                    TaskModels.save(i)
                else:
                    i.status = ustatus
                    i.completed = None
                    TaskModels.save(i)
                return redirect('http://127.0.0.1:8000/users/member/')
        
    else:
        return render(request, 'users/updatestatus.html')


def alltasks(request):
    alltasks = TaskModels.objects.all()
    

    return render(request, 'users/alltasks.html', {'tasks': alltasks})