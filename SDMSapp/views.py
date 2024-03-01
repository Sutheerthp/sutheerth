
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from .forms import PlayerForm, Player, DepartmentForm, Sportform
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *

class StudentCreateView(CreateView):
    form_class = StudentForm
    #path('add_player/', add_player, name='addplayer'),
    success_url = reverse_lazy('StudentCreateView')  # Replace 'success_url_name' with the name of the URL to redirect after successful creation
    template_name = 'SDMSapp/student_form.html'  # Replace 'SDMSapp/student_form.html' with the path to your template file

    def form_valid(self, form):
        # Custom logic if the form is valid
        return super().form_valid(form)

    def form_invalid(self, form):
        # Custom logic if the form is invalid
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('success_url_name')  # Replace 'success_url_name' with the name of the URL to redirect after successful deletion
    template_name = 'SDMSapp/student_confirm_delete.html'  # Replace 'your_app/student_confirm_delete.html' with the path to your template file

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'year_of_admission', 'admission_no', 'programme_id', 'uty_reg_no','dob', 'place', 'city', 'district', 'pincode']
    success_url = reverse_lazy('success_url_name')  # Replace 'success_url_name' with the name of the URL to redirect after successful update
    template_name = 'SDMSapp/student_form.html'  # Replace 'your_app/student_form.html' with the path to your template file



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

# def add_player(request):
#     if request.method == 'POST':
#         form = PlayerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('SDMSapp/player_list')  # Redirect to player list page after successful form submission
#     else:
#         form = PlayerForm()
#     return render(request, 'SDMSapp/addplayer.html', {'form': form})

# def player_list(request):
#     players = Player.objects.all()
#     return render(request, 'SDMSapp/player_list.html', {'players': players})



