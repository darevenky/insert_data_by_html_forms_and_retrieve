from django.db import models

# Create your models here.

class Team(models.Model):

    ipl_team=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return self.ipl_team

class Details(models.Model):

    ipl_team=models.ForeignKey(Team,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    loc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
