from django.db import models

class Status(models.TextChoices):
    ToDo = 'ToDo', 'todo'
    InProgress = 'In Progress', 'in progress'
    Completed = 'Completed', 'completed'
    Tested = 'Tested', 'tested'
    Rejected = 'Rejected', 'rejected'
    Done = 'Done', 'done'
    Backlog = 'Backlog', 'backlog'


class Project(models.Model):
    objects = " "
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'project'


class Task(models.Model):
    objects = None
    name= models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        choices=Status.choices,
        max_length=20,
        default=Status.ToDo
    )
    to_user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'task'