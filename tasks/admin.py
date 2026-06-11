from django.contrib import admin
from tasks.models import Project


# Register your models here.
@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    pass