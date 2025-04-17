from django.shortcuts import render

from .forms import StudentForm
from django.shortcuts import get_object_or_404
from common_App.models import Courses, OngoingCourses
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse
from common_App.models import *



def courses(request):
    active_courses=Courses.objects.filter(is_active = "Active Now")
    soon_courses=Courses.objects.filter(is_active = "Coming Soon")
    context={'activecoursesList':active_courses,'sooncoursesList':soon_courses}
    return render (request,'StudentsApp/courses.html',context)


def StudentApplication(request, course_id):
    course_instance = get_object_or_404(Courses, id=course_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, course_instance=course_instance)
        if form.is_valid():
            student = form.save()
            return redirect('success_page')  # Replace with your real redirect
    else:
        form = StudentForm(course_instance=course_instance)

    return render(request, 'StudentsApp/ApplicationForm.html', {
        'form': form,
        'selected_course': course_instance, 
    })
def courseDetails(request,course_id):
    course_details=Courses.objects.get(id=course_id)
    context={'course':course_details}
    return render (request,'StudentsApp/CourseDetails.html',context)


def courseByAge(request,course_age):
    filtered_courses_by_age = Courses.objects.filter(age=course_age)
    context= {'filtered_courses_by_age': filtered_courses_by_age}
    return render(request,'StudentsApp/filteredCourses.html',context )


def courseByCategory(request,course_category):
    filtered_courses_by_category = Courses.objects.filter(category=course_category)
    context= {'filtered_courses_by_category': filtered_courses_by_category}
    return render(request,'StudentsApp/filteredCourses.html',context )