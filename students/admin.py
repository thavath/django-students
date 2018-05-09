from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Student)
admin.site.register(Experience)
admin.site.register(Family)
admin.site.register(Attendance)
admin.site.register(Fujiyama)
admin.site.register(Interview)