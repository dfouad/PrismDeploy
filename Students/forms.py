from django import forms
from common_App.models import Student, OngoingCourses

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['studentID']  # Remove studentID from the form
        widgets = {
            'dateofbirth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control border-0'}),
            'name': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'school': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'grade': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'parentContact': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'address': forms.Textarea(attrs={'class': 'form-control border-0', 'style': 'height: 100px'}),
            'course': forms.Select(attrs={'class': 'form-control border-0'}),
        }

    def __init__(self, *args, **kwargs):
        course_instance = kwargs.pop('course_instance', None)
        super().__init__(*args, **kwargs)
        if course_instance:
            # Set initial value for the course field
            self.initial['course'] = course_instance.pk




