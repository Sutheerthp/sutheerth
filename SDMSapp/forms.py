from django import forms
from .models import Department, Programme, Stud_item, Student, Item




# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = '__all__'

# class Sportform(forms.ModelForm):
#     class Meta:
#         model = Sport
#         fields = '__all__'


# class PlayerForm(forms.ModelForm):
#     class Meta:
#         fields = ['dob']
#         widgets = {
#             'dob': forms.DateInput(attrs={'type': 'date'}),
#         }
#         model = Player
#         fields = '__all__'  # Use all fields from the Player model