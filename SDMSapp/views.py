from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from SDMSapp.models import Student



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
        # Extract student data from the request
        name = request.POST.get('name')
        year_of_admission = request.POST.get('year_of_admission')
        admission_no = request.POST.get('admission_no')
        programme_id = request.POST.get('programme_id')
        uty_reg_no = request.POST.get('uty_reg_no')
        place = request.POST.get('place')
        city = request.POST.get('city')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')

        # Create a new Programme instance or get an existing one based on form data
        programme_instance = Programme.objects.get(id=programme_id)

        # Create a new Student instance
        new_student = Student(
            name=name,
            year_of_admission=year_of_admission,
            admission_no=admission_no,
            programme_id=programme_instance,
            uty_reg_no=uty_reg_no,
            place=place,
            city=city,
            district=district,
            pincode=pincode
        )

        # Save the new student instance
        new_student.save()

        return redirect(reverse('success_page'))  # Redirect to the success page
    else:
        # Render the form template (assuming you have a template for the form)
        return render(request, 'SDMSapp/home.html')

def success_page(request):
    return render(request, 'SDMSapp/success_page.html')

def edit_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('selected_student')
        student = get_object_or_404(Student, student_id=student_id)

        # Update the student instance with new data
        student.name = request.POST.get('name')
        student.year_of_admission = request.POST.get('year_of_admission')
        student.admission_no = request.POST.get('admission_no')
        student.programme_id = request.POST.get('programme_id')
        student.uty_reg_no = request.POST.get('uty_reg_no')
        student.place = request.POST.get('place')
        student.city = request.POST.get('city')
        student.district = request.POST.get('district')
        student.pincode = request.POST.get('pincode')

        # Save the updated student instance
        student.save()

        return redirect('student_list')  # Redirect to the student list page after editing
    else:
        students = Student.objects.all()
        return render(request, 'SDMSapp/edit_student.html', {'students': students})

