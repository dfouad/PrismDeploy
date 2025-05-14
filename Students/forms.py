from django import forms
from common_App.models import Student, Courses  # Ensure Courses is imported

class StudentForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Courses.objects.all(),
        widget=forms.HiddenInput(),
        required=True
    )

    class Meta:
        model = Student
        exclude = ['studentID']
        widgets = {
            'dateofbirth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control border-0'}),
            'name': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'school': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'grade': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'parentContact': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'address': forms.Textarea(attrs={'class': 'form-control border-0', 'style': 'height: 100px'}),
        }

    def __init__(self, *args, **kwargs):
        course_instance = kwargs.pop('course_instance', None)
        super().__init__(*args, **kwargs)
        if course_instance:
            self.initial['course'] = course_instance.pk  # Ensure course ID is correctly passed
            self.fields['course'].initial = course_instance.pk  # Set the initial value
