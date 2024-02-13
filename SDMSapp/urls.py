from django.urls import path
from .views import user_login, user_signup, user_home,add_player

urlpatterns = [
    path('login/home/', user_home, name='home'),
    path('login/', user_login, name='login'),
    path('login/signup/', user_signup, name='signup'),
    path('add_player/', add_player, name='add_player'),
]
