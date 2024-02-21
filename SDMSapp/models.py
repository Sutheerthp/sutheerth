from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    sl_no = models.AutoField(primary_key=True)
    stud_name = models.CharField(max_length=100)
    stud_id = models.CharField(max_length=20, unique=True)  # Assuming stud_id is a unique identifier
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dob = models.DateField()
    year = models.IntegerField()
    place = models.CharField(max_length=100)
    PLAYER_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    player_status = models.CharField(max_length=10, choices=PLAYER_STATUS_CHOICES, default='Active')
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    position = models.IntegerField()
    selected_to_university = models.BooleanField(default=False)
    graduation_level = models.CharField(max_length=50)

    def __str__(self):
        return self.stud_name
