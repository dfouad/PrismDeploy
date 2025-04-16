from django.urls import path,include
from . import views


urlpatterns = [
    
    path('courses', views.courses,name='courses'),
    path('courseDetails/<str:course_id>/', views.courseDetails,name='courseDetails'),
    path('courseByAge/<str:course_age>/', views.courseByAge,name='courseByAge'),
    path('courseByCategory/<str:course_category>/', views.courseByCategory,name='courseByCategory'),
    path('application/<str:course_id>', views.StudentApplication,name='application'),
    
]