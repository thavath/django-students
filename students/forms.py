from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceForm(ModelForm):
	class Meta:
		model = Attendance
		fields = '__all__'


class InterviewForm(ModelForm):
	class Meta:
		model = Interview
		fields = '__all__'

class FujiyamaForm(ModelForm):
	class Meta:
		model = Fujiyama
		fields = '__all__'
		
class FamilyForm(ModelForm):
	class Meta:
		model = Family
		fields = '__all__'
					
class ExperienceForm(ModelForm):
	class Meta:
		model = Experience
		fields = '__all__'