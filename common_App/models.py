from django.db import models

import datetime

from multiselectfield import MultiSelectField # type: ignore

# Create your models here.



class Component(models.Model):
   
   name          = models.CharField(max_length=50,null=True)
   image         = models.ImageField(null=True,blank=True)


   @property
   def imageURL(self):
        try:
            url =self.picture.url
        except:
            url =''
        return url  



class ToolKit(models.Model):

    kitID      = models.IntegerField(null=True)
    level      = models.IntegerField(null=True)
    details    = models.TextField(max_length=1000,null=True)
    price      = models.IntegerField(null=True)
    components = models.ManyToManyField(Component)

    def __str__(self):
        return "level"+str(self.level) 


class Centers(models.Model):

    name          = models.CharField(max_length=50,null=True)
    phone         = models.IntegerField(null=True)
    location      = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name  
    



class Courses(models.Model):
  
      
 
  age = (
      ("5-7","5-7"),
      ("7-9","7-9"),
      ("9-11","9-11"),
      ("11-13","11-13"),
      ("13+","13+")
  )

  type = (
        ("Online Course","Online"),
        ("On-Site Course","Offline"),
    )     
  
  category = (
               ("Programming","Programming"),
               ("Robotics","Robotics"),
               ("Strong Mind","Strong Mind"),
      
             )
  
  is_active =( ("Active Now","Active Now"),
               ("Coming Soon","Coming Soon"),
      
        )
  name          = models.CharField(max_length=50,null=True)
  description   = models.TextField(max_length=400,null=True)
  course_overview   = models.TextField(max_length=400,null=True)
  what_you_will_learn = models.TextField(max_length=800,null=True)
  requirments   = models.TextField(max_length=200,null=True)
  course_duration   = models.TextField(max_length=200,null=True)
  session_duration  = models.TextField(max_length=  200,null=True)
  level         = models.IntegerField(null=True)
  price         = models.IntegerField(null=True)
  kitId         = models.OneToOneField(ToolKit,null=True,blank=True,on_delete=models.CASCADE)
  maxNmberofstudents        = models.IntegerField(null=True)
  CourseStatus = models.CharField(max_length=50,choices=type,null=True)
  age = MultiSelectField(max_length=50,choices=age)
  category = models.CharField(max_length=50,choices=category,null=True)
  image         = models.ImageField(null=True,blank=True)
  is_active     = models.CharField(max_length=50,choices=is_active,null=True)
  hours_per_month = models.IntegerField(null=True)

  def __str__(self):
        return self.name  

  
class Instractor(models.Model):

    name          = models.CharField(max_length=50,null=True)
    phone         = models.IntegerField(null=True)
    location      = models.CharField(max_length=50,null=True)
    courses       = models.ManyToManyField(Courses)

    def __str__(self):
        return self.name
    


class OngoingCourses(models.Model):
  WEEKDAYS = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
  age = [
      ("5-7","5-7"),
      ("7-9","7-9"),
      ("9-11","9-11"),
      ("11-13","11-13"),
      ("13+","13+")
  ]
  courseID       = models.ForeignKey(Courses,null=True,blank=True,on_delete=models.SET_NULL)
  instractor     = models.ForeignKey(Instractor,null=True,blank=True,on_delete=models.SET_NULL)
  location       = models.ForeignKey(Centers,null=True,blank=True,on_delete=models.SET_NULL)
  WeekDay        = models.CharField(max_length=3, choices=WEEKDAYS, default='MON')
  age        = models.CharField(max_length=6, choices=age, default='5-7')
  start_time = models.TimeField(default=datetime.time(0, 0))
  end_time   = models.TimeField(default=datetime.time(0, 0))
  startDate      = models.DateField()
  paymentMethod  = models.CharField(max_length=20,null=True)
  sessionNumber  = models.IntegerField(null=True)

  def __str__(self):
        return f"{self.courseID} on {self.get_WeekDay_display()} at {self.start_time}"
  



class Student(models.Model):

    name          = models.CharField(max_length=50,null=True)
    phone         = models.IntegerField(null=True)
    dateofbirth   = models.DateField()
    school        = models.CharField(max_length=50,null=True)
    grade         = models.CharField(max_length=50,null=True)
    parentContact = models.IntegerField(null=True)
    address       = models.TextField(max_length=200,null=True)
    studentID     = models.IntegerField(null=True)
    Enrolled_Course        = models.ManyToManyField(OngoingCourses)
    paid_fees         = models.BooleanField(default=False)
    paying_image           = models.ImageField(upload_to='student_images/', null=True, blank=True)



    def __str__(self):
        return self.name
    






  

