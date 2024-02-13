from django.db import models

class Player(models.Model):
    sl_no = models.AutoField(primary_key=True)
    stud_name = models.CharField(max_length=100)
    stud_id = models.CharField(max_length=20, unique=True)  # Assuming stud_id is a unique identifier
    SPORT_DETAILS = [('sport','sport'),
                     ('kabaddi','kabaddi'),
                     ('basketball','basketball'),
                     ('handball','handball'), 
                     ('cricket','cricket'),
                     ('football','football'),
                     ('ball_batminton','ball_batminton'),
                     ('shuttle_batminton','shuttle_batminton'),
                     ('wrestling','wrestling'),
                     ('judo','judo'),
                     ('taekwondo','taekwondo'),
                     ('karate','karate'),
                     ('Kho-kho','kho-kho')
    ]
    sport = models.CharField(max_length=50, choices=SPORT_DETAILS, default='Active')
    DEPT_DETAILS = (("computer_science", "Computer Science"),
                    ("physics", "Physics"),
                    ("mathematics", "Mathematics"),
                    ("statistics", "Statistics"),
                    ("malayalam", "Malayalam"),
                    ("history", "History"),
                    ("zoology", "Zoology"),
                    ("plantsciece", "Plantsciece"),
                    ("polymer_chemistry", "Polymer Chemistry"),
                    ("economics", "Economics"),
                    ("commerce", "Commerce"),
                    ("english", "English")
)


    department = models.CharField(max_length=100, choices=DEPT_DETAILS, default=True)
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
