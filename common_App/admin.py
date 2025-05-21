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


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Fields to display in the admin list page columns
    list_display = ('id', 'name', 'phone', 'grade', 'school', 'paid_fees', 'show_courses')

    # Fields to filter the list by in the sidebar
    list_filter = ('grade', 'school', 'paid_fees')

    # Actions available in the dropdown to perform on selected objects
    actions = ['mark_as_paid']

    # Fields searchable in the admin search box
    search_fields = ('name', 'school', 'studentID')

    # Fields displayed and editable on the admin form page
    fields = (
        'name', 'phone', 'dateofbirth', 'school', 'grade',
        'parentContact', 'address', 'studentID', 'Enrolled_Course',
        'paid_fees', 'paying_image'
    )

    # Fields displayed as read-only in the admin form (non-editable)
    readonly_fields = ('studentID',)

    # Custom method to show all courses a student is enrolled in, joined as a string
    def show_courses(self, obj):
        # Convert each enrolled course to string (uses course's __str__) and join with commas
        return ", ".join(str(course) for course in obj.Enrolled_Course.all())

    # Set the column header name for show_courses in the list view
    show_courses.short_description = 'Courses'

    # Define a custom action for the admin list view, with description shown in dropdown
    @admin.action(description='Mark selected students as paid')
    def mark_as_paid(self, request, queryset):
        # Update the paid_fees field to True for all selected students
        updated = queryset.update(paid_fees=True)
        # Show a message in the admin after action completes, with count of updated records
        self.message_user(request, f"{updated} student(s) marked as paid.")
