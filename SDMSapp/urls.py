from django.urls import path
from .views import user_login, user_signup, user_home,add_player, player_list

urlpatterns = [
    path('home/', user_home, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('add_player/', add_player, name='addplayer'),
    path('playerlist', player_list, name='playerlist')
]
