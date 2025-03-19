from django.shortcuts import render
from common_App.models import Courses


def courses(request):
    all_courses=Courses.objects.filter(is_active =True)
    context={'coursesList':all_courses}
    return render (request,'studentsapp/courses.html',context)


def courseDetails(request,course_id):
    course_details=Courses.objects.get(id=course_id)
    context={'course':course_details}
    return render (request,'studentsapp/courseDetails.html',context)