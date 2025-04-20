from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=255)

class Team(models.Model):
    number_member = models.IntegerField(default=0)
    members_name = models.TextField()
    project = models.ForeignKey(Projects , on_delete=models.CASCADE)