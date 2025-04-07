from django.shortcuts import render
from common_App.models import Courses


def courses(request):
    active_courses=Courses.objects.filter(is_active = "Active Now")
    soon_courses=Courses.objects.filter(is_active = "Coming Soon")
    context={'activecoursesList':active_courses,'sooncoursesList':soon_courses}
    return render (request,'StudentsApp/courses.html',context)


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