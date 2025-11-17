from django import forms
from .models import PYQ

class PYQForm(forms.ModelForm):
    class Meta: 
        model = PYQ
        fields = ['course_name', 'subject_name', 'year', 'pyq_file']
        labels = {
            'course_name': 'Course (e.g., BCA, BTech)',
            'subject_name': 'Subject (e.g., Data Structures)',
            'year': 'Year',
            'pyq_file': 'Upload file (PDF, JPG)'
        }

