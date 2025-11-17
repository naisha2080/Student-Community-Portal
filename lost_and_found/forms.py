from django import forms
from .models import LostFoundItem

class LostFoundForm(forms.ModelForm):
    class Meta:
        model = LostFoundItem
        fields = ['status', 'item_name','image', 'description', 'location']
        labels = {
            'status': 'Did you lose or found this item ?',
            'item_name': 'What is this item ?',
            'description': 'Description (color, brand, etc)',
            'image': 'Add a picture',
            'location': 'Where did you lose/find it ?',  
        }

