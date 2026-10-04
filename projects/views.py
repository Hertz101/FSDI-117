from django.shortcuts import render

# from . import models      Can work as well
from .models import Project, Skill


# Create your views here.
def projects_view(request):
  projects_list = Project.objects.all().order_by('-year')
  context = {"projects": projects_list}
  return render(request, "projects/projects.html", context)



# projects_list = models.Project.object.all().order_by('-year)