from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from app.models import *

def team(request):

    if request.method=='POST':

        tn=request.POST['name']

        TO=Team.objects.get_or_create(ipl_team=tn)[0]
        TO.save()

        return HttpResponse('<h2>Team is added successfully</h2>')
        
    return render(request,'team.html')


def details(request):
    DO=Team.objects.all()
    d={'DO':DO}

    if request.method=='POST':

        team=request.POST['team']
        name=request.POST['name']
        age=request.POST['age']
        loc=request.POST['loc']

        TO=Team.objects.get(ipl_team=team)

        DEO=Details.objects.get_or_create(ipl_team=TO,name=name,age=age,loc=loc)[0]
        DEO.save()

        return HttpResponse('<h2> Details are successfully submitted')

    return render(request,'details.html',d)




def retrieve(request):
    DO=Team.objects.all()
    d={'DO':DO}

    if request.method=='POST':
        team=request.POST.getlist('team')

        query=Details.objects.none()

        for i in team:
            query=query|Details.objects.filter(ipl_team=i)
        
        d1={'det':query}

        return render(request,'display.html',d1)


    return render(request,'retrieve.html',d)
