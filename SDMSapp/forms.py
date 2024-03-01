from django import forms
from .models import Department, Programme, Student, Item, Stud_item



class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['name', 'dept']

class StudentForm(forms.ModelForm):
    year_of_admission = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Student
        fields = ['name', 'year_of_admission', 'admission_no', 'dob', 'programme_id', 'uty_reg_no', 'place', 'city', 'district', 'pincode']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_type', 'no_of_players', 'position', 'year']
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date'}),
        }

class StudItemForm(forms.ModelForm):
    class Meta:
        model = Stud_item
        fields = ['item_id', 'player_status', 'uty_team_selection']





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