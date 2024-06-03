from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from SDMSapp.models import Student
from .forms import StudentForm
from .forms import SearchForm


#from .forms import PlayerForm, Player, DepartmentForm, Sportform


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Handle invalid login
            return render(request, 'SDMSapp/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'SDMSapp/login.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'SDMSapp/signup.html', {'form': form})

@login_required
def user_home(request):
    return render(request, 'SDMSapp/home.html')


from django.shortcuts import render, redirect
from SDMSapp.models import Student, Programme  # Import your models

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the list of students after adding
    else:
        form = StudentForm()
    return render(request, 'SDMSapp/addstudent.html', {'form': form})
def success_page(request):
    return render(request, 'SDMSapp/success_page.html')

def edit_student(request, uty_reg_no):
    student = get_object_or_404(Student, uty_reg_no=uty_reg_no)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list page after editing
    else:
        form = StudentForm(instance=student)
    return render(request, 'SDMSapp/edit_student.html', {'student': student})

def view_student(request):
    # Query all student records
    students = Student.objects.all()
    return render(request, 'SDMSapp/view_student.html', {'students': students})

def search_student(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            uty_reg_no = form.cleaned_data['uty_reg_no']
            return redirect('edit_student', uty_reg_no=uty_reg_no)
    else:
        form = SearchForm()
    return render(request, 'search_student.html', {'form': form})