# forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class SearchForm(forms.Form):
    uty_reg_no = forms.CharField(label='Enter Registration Number', max_length=50)



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