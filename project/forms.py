from django import forms
from project.models import Project

class CreateProjectForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField()

    class Meta:
        model = Project
        fields = ('name', 'description')