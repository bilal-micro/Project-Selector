from django.contrib import admin
from .models import Projects, Team

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'members_name', 'project')
    search_fields = ('members_name',)
    list_filter = ('project',)
