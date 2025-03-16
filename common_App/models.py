from django.db import models

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

    kitID      = models.IntegerField(max_length=10,null=True)
    level      = models.IntegerField(max_length=5,null=True)
    details    = models.TextField(max_length=100,null=True)
    price      = models.IntegerField(max_length=50,null=True)
    components = models.ManyToManyField(Component)



class Centers(models.Model):

    name          = models.CharField(max_length=50,null=True)
    phone         = models.IntegerField(max_length=15,null=True)
    location      = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name  
    



class Courses(models.Model):
  type = (
        ("Online Course","Online"),
        ("On-Site Course","Offline"),
    )
  
  name          = models.CharField(max_length=50,null=True)
  description   = models.TextField(max_length=200,null=True)
  level         = models.IntegerField(max_length=5,null=True)
  price         = models.IntegerField(max_length=10,null=True)
  kitId         = models.OneToOneField(ToolKit,null=True,blank=True,on_delete=models.CASCADE)
  minAge        = models.IntegerField(max_length=10,null=True)
  maxNmberofstudents        = models.IntegerField(max_length=20,null=True)
  status        = models.CharField(max_length=50,null=True)
  CourseStatus = models.CharField(max_length=50,choices=type,null=True)
  image         = models.ImageField(null=True,blank=True)
  is_active     = models.BooleanField(default=False)

  def __str__(self):
        return self.name    


class Instractor(models.Model):

    name          = models.CharField(max_length=50,null=True)
    phone         = models.IntegerField(max_length=15,null=True)
    location      = models.CharField(max_length=50,null=True)
    paymentMethod = models.CharField(max_length=20,null=True)
    courses       = models.ManyToManyField(Courses)

    def __str__(self):
        return self.name
    


class OngoingCourses(models.Model):

  courseID       = models.ForeignKey(Courses,null=True,blank=True,on_delete=models.SET_NULL)
  instractor     = models.ForeignKey(Instractor,null=True,blank=True,on_delete=models.SET_NULL)
  location       = models.ForeignKey(Centers,null=True,blank=True,on_delete=models.SET_NULL)
  WeekDay        = models.CharField(max_length=50,null=True)
  startDate      = models.DateField()
  paymentMethod  = models.CharField(max_length=20,null=True)
  sessionNumber  = models.IntegerField(max_length=10,null=True)

  def __str__(self):
        return self.name  
  



class Student(models.Model):

    name          = models.CharField(max_length=50,null=True)
    phone         = models.IntegerField(max_length=15,null=True)
    dateofbirth   = models.DateField()
    school        = models.CharField(max_length=50,null=True)
    grade         = models.CharField(max_length=50,null=True)
    parentContact = models.IntegerField(max_length=15,null=True)
    address       = models.TextField(max_length=200,null=True)
    studentID     = models.IntegerField(max_length=15,null=True)
    course        = models.ManyToManyField(OngoingCourses)


    def __str__(self):
        return self.name
    






  

