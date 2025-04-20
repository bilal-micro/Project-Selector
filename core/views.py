from django.shortcuts import render
from app.models import Projects , Team
from django.http import HttpResponseBadRequest , HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def render_index(request):
    projects = Projects.objects.all()
    team = Team.objects.all()
    for t in team:
        projects = projects.exclude(id = t.project.id)
    return render(request= request , template_name='form.html' , context={
        'projects' : projects
    })

@csrf_exempt
def submit_new(request):
    if request.method == "POST":
        print(request.body)

        data = json.loads(request.body.decode())
        members_name = data.get('teamName')
        p = data.get('project')
        number_member = data.get('numberMember')
        ch = Team.objects.filter(project = Projects.objects.get(name = p)).first()
        if ch:
            return HttpResponseBadRequest()
        Team.objects.create(
            members_name = members_name,
            project = Projects.objects.get(name = p),
            number_member = number_member
           ).save()
        return HttpResponse()
    