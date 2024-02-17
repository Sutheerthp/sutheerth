# player_management/admin.py

from django.contrib import admin
from .models import Player, Department, Sport

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('sl_no', 'stud_name', 'sport', 'department', 'dob', 'year', 'place', 'player_status', 'gender', 'position', 'selected_to_university', 'graduation_level')
    list_filter = ('sport', 'department', 'player_status', 'gender', 'selected_to_university')
    search_fields = ('stud_name', 'sport', 'department', 'position')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Department)
admin.site.register(Sport)
