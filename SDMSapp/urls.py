from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', user_home, name='home'),
    #path('signup/', user_signup, name='signup'),
    path('student_delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('student_update/', StudentUpdateView.as_view(), name='StudentUpdateView'),
    path('studentCreate/', StudentCreateView.as_view(), name='StudentCreateView'),
    #path('add_player/', add_player, name='addplayer'),
    #path('playerlist/', player_list, name='playerlist')
]