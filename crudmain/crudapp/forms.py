from django import forms
from crudapp import models

class StudentForms(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"