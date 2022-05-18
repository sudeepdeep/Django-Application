from django.contrib import admin
from .models import CreateUser, CreateTeam, CreateTask, TeamModel, TaskModels

admin.site.register(CreateUser)
admin.site.register(CreateTask)
admin.site.register(TeamModel)
admin.site.register(TaskModels)
