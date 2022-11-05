from django.shortcuts import render
from crudapp import forms
from crudapp.models import Student

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('first_name')
    diction = {'title': 'Index', 'student_list':student_list}
    return render(request, 'app_1/index.html', context=diction)

def student_form(request):
    form = forms.StudentForms()

    if request.method == 'POST':
        form = forms.StudentForms(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title': 'Student Form',"student_form":form}
    return render(request, 'app_1/student_form.html', context=diction)

def student_info(request,student_id):
    student_info = Student.objects.get(pk=student_id)
    diction = {'student_info': student_info}
    return render(request,'app_1/student_info.html', context=diction)

def student_update(request,student_id):
    student_info = Student.objects.get(pk=student_id)
    form = forms.StudentForms(instance=student_info)

    if request.method == 'POST':
        form = forms.StudentForms(request.POST, instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'student_form':form}
    return render(request,'app_1/student_update.html', context=diction)

def student_delete(request,student_id):
    student = Student.objects.get(pk=student_id).delete()
    diction = {'delete_message': "Delete Done"}
    return render(request,'app_1/student_delete.html', context=diction)