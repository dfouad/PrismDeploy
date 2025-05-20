from django import forms
from common_App.models import Student

# Define a ModelForm for the Student model
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # Exclude fields that will be set manually in the view
        exclude = ['studentID', 'Enrolled_Course']
        widgets = {
            # Use date input with Bootstrap styling
            'dateofbirth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control border-0'}),
            'name': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'school': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'grade': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'parentContact': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'address': forms.Textarea(attrs={'class': 'form-control border-0', 'style': 'height: 100px'}),
            # Checkbox with JS trigger for showing/hiding payment proof
            'paid_fees': forms.CheckboxInput(attrs={'class': 'form-check-input', 'onchange': "togglePaymentProof()"}),
            # File input for uploading payment proof
            'paying_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make payment proof optional by default
        self.fields['paying_image'].required = False

    def clean(self):
        cleaned_data = super().clean()
        paid_fees = cleaned_data.get("paid_fees")
        paying_image = cleaned_data.get("paying_image")

        # Require payment proof if fees are marked as paid
        if paid_fees and not paying_image:
            self.add_error('paying_image', "Payment proof is required when fees are marked as paid")
        return cleaned_data
