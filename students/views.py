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

def interview(request, pk=None):
    student = get_object_or_404(Student, pk=pk)
    interviews = get_list_or_404(Interview, student = student)
    context = { 'student' : student, 'interviews' : interviews }
    return render(request, 'students/interview.html', context )
    
def experience(request, pk=None):
    student = get_object_or_404(Student, pk=pk)
    experiences = get_list_or_404(Experience, student = student)
    context = { 'student' : student, 'experiences' : experiences }
    return render(request, 'students/experience.html', context )

def family(request, pk=None):
    student = get_object_or_404(Student, pk=pk)
    families = get_list_or_404(Family, student = student)
    context = { 'student' : student, 'families' : families }
    return render(request, 'students/family.html', context )

def fujiyama(request, pk=None):
    student = get_object_or_404(Student, pk=pk)
    fujiyamas = get_list_or_404(Fujiyama, student = student)
    context = { 'student' : student, 'fujiyamas' : fujiyamas }
    return render(request, 'students/fujiyama.html', context )
    # NEW STUDENT INFORMATION
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

def new_interview(request):
    if request.method == "POST":
        formI = InterviewForm(request.POST)
        context = { 'formI': formI }
        if formI.is_valid():
            formI = formI.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/new_interview.html', context)
    else:
        formI = InterviewForm()
        context = { 'formI' : formI }
        return render(request, 'students/new_interview.html', context)
        
def new_experience(request):
    if request.method == "POST":
        formE = ExperienceForm(request.POST)
        context = { 'formE': formE }
        if formE.is_valid():
            formE = formE.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/new_experience.html', context)
    else:
        formE = ExperienceForm()
        context = { 'formE' : formE }
        return render(request, 'students/new_experience.html', context)

def new_family(request):
    if request.method == "POST":
        formF= FamilyForm(request.POST)
        context = { 'formF': formF }
        if formF.is_valid():
            formF = formF.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/new_family.html', context)
    else:
        formF = FamilyForm()
        context = { 'formF' : formF }
        return render(request, 'students/new_family.html', context)
        
def new_fujiyama(request):
    if request.method == "POST":
        formFu= FujiyamaForm(request.POST)
        context = { 'formFu': formFu }
        if formFu.is_valid():
            formFu = formFu.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/new_fujiyama.html', context)
    else:
        formFu = FamilyForm()
        context = { 'formFu' : formFu }
        return render(request, 'students/new_fujiyama.html', context)
        
# EDIT PAGE ====================================================================
def edit_student(request, pk=None):
    student = get_object_or_404(Student,pk=pk)
    if request.method == "POST":
        formS = StudentForm(request.POST, instance=student)
        context = { 'formS': formS }
        if formS.is_valid():
            formS = formS.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/edit_student.html', context)
    else:
        formS = StudentForm(instance=student)
        context = { 'formS' : formS }
        return render(request, 'students/edit_student.html', context)
    
def edit_interview(request, pk=None):
    student = get_object_or_404(Student,pk=pk)
    if request.method == "POST":
        formI = InterviewForm(request.POST, instance=student)
        context = { 'formI': formI }
        if formI.is_valid():
            formI = formI.save()
            return HttpResponseRedirect(reverse('students:index'))
        else:
            return render(request, 'students/edit_interview.html', context)
    else:
        
        formI = InterviewForm(instance=student)
        context = { 'formI' : formI }
        return render(request, 'students/edit_interview.html', context)