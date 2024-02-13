from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        fields = ['dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
        model = Player
        fields = '__all__'  # Use all fields from the Player model
