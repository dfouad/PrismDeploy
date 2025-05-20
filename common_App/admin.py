from django.contrib import admin
from .models import*
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(Component)
admin.site.register(ToolKit)
admin.site.register(Centers)
admin.site.register(Courses)
admin.site.register(Instractor)
#admin.site.register(OngoingCourses)
#admin.site.register(Student)

class OngoingCoursesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      ...

admin.site.register(OngoingCourses,OngoingCoursesAdmin )


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      ...

admin.site.register(Student,StudentAdmin )