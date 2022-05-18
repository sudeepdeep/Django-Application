from django.db import models

class CreateUser(models.Model): #here we register the user with the roles
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.role

class CreateTeam(models.Model): #creation of the team by the user
    teamname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class CreateTask(models.Model): #creating the task by the user after login
    taskname = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.team


class TeamModel(models.Model): #this is the team model where both TL and TM present
    name = models.CharField(max_length=255)
    teamname = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role



class TaskModels(models.Model): #after the teamlead assign the task to members it is stored here
    name = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    taskdesc = models.TextField()
    started = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


