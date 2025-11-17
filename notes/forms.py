from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['course_name', 'subject_name', 'topic_name', 'note_file']
        labels = {
            'course_name': 'Course (e.g, BCA, BTech, BSc Maths)',
            'subject_name': 'Subject (e.g, DSA, OOP with Java, DBMS)',
            'topic_name': 'Topic name (Unit-1, Sorting techniques)',
            'note_file': 'Upload notes (PDF, DOCx, etc.)'
        }