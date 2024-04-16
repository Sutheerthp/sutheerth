from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', user_home, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('add_student/', add_student, name='add_student'),
    path('success_page/', success_page, name='success_page'),
    path('edit_student/', edit_student, name='edit_student')
]