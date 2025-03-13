from django.shortcuts import render

# Create your views here.
def courses(request):
    return render (request,'studentsapp/courses.html')


def courseDetails(request):
    return render (request,'studentsapp/courseDetails.html')