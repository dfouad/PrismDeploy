from django.shortcuts import render

from .forms import StudentForm
from django.shortcuts import get_object_or_404
from common_App.models import Courses, OngoingCourses
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse
from common_App.models import *

from django.http import JsonResponse
from django.template.loader import render_to_string


def courses(request):
    courses=Courses.objects.all().order_by('is_active')
    context={'coursesList':courses}
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


def courseByAge(request):
    course_age = request.GET.get('course_age')
    print('course_age',course_age )
    courses_by_age = Courses.objects.filter(age__contains=course_age)
    print(f"[DEBUG] Filtered courses for age '{course_age}': {[course.name for course in courses_by_age]}")
    html = render_to_string('StudentsApp/filteredCourses.html', {'coursesList':courses_by_age})
    print('html',html )
    return JsonResponse({'html':html})


def courseByCategory(request):
    course_category = request.GET.get('course_category')
    print('course_category',course_category )
    courses_by_category = Courses.objects.filter(category=course_category)
    print(f"[DEBUG] Filtered courses for age '{course_category}': {[course.name for course in courses_by_category]}")
    html = render_to_string('StudentsApp/filteredCourses.html', {'coursesList':courses_by_category})
    print('html',html )
    return JsonResponse({'html':html})
