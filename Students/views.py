from django.shortcuts import render
from common_App.models import Courses


def courses(request):
    active_courses=Courses.objects.filter(is_active = "Active Now")
    soon_courses=Courses.objects.filter(is_active = "Coming Soon")
    context={'activecoursesList':active_courses,'sooncoursesList':soon_courses}
    return render (request,'studentsapp/courses.html',context)


def courseDetails(request,course_id):
    course_details=Courses.objects.get(id=course_id)
    context={'course':course_details}
    return render (request,'studentsapp/courseDetails.html',context)