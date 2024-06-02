from django import forms
from . models import Module, Course


class UniversityForm(forms.Form):

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        initial=Course.objects.first()
    )
