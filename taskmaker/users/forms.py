from django import forms
from . import models

#creation of the team 

class CreateNewTeam(forms.Form):
    teamname = forms.CharField(max_length=255)



#creation of the task
# class CreateNewTask(forms.ModelForm):
    # class Meta:
    #     model = models.CreateTask
    #     fields = ['taskname', 'team', 'description']