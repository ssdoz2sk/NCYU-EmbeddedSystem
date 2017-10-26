from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateProjectForm
from .models import Project

from device import forms
# Create your views here.

@login_required
def project(request):
    projects = Project.objects.filter(creater=request.user)
    return render(request,
                  'project/project.html',
                  {'projects': projects})

@login_required
def new_project(request):
    if request.method == 'POST':
        project_form = CreateProjectForm(request.POST)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            new_project.creater = request.user
            new_project.save()
            return redirect(new_project)
    else:
        project_form = CreateProjectForm()

    return render(request,
                  'project/new_project.html',
                  {'project_form': project_form})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project/project_detail.html', {'project': project})