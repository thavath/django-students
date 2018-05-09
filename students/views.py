from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = { 'students': students }
    return render(request, 'students/index.html', context)

def detail(request,pk=None):
    student = Student.objects.get(pk=pk)
    context = {'student': student }
    return render(request, 'students/detail.html', context)

def attendance(request, pk=None):
    student = get_object_or_404(Student, pk=pk)
    attendances = get_list_or_404(Attendance, student = student)
    context = { 'student' : student, 'attendances' : attendances }
    return render(request, 'students/attendance.html', context )

def new_student(request):
    if request.method == "POST":
        formS = StudentForm(request.POST)
        context = { 'formS': formS }
        if formS.is_valid():
            formS = formS.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/new_student.html', context)
    else:
        formS = StudentForm()
        context = { 'formS' : formS }
        return render(request, 'students/new_student.html', context)

def new_attendance(request):
    if request.method == "POST":
        formA = AttendanceForm(request.POST)
        context = { 'formA': formA }
        if formA.is_valid():
            formA = formA.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/new_attendance.html', context)
    else:
        formA = AttendanceForm()
        context = { 'formA' : formA }
        return render(request, 'students/new_attendance.html', context)