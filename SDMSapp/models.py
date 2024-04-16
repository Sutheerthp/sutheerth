from django.db import models

class Department(models.Model):
    dept_id = models.IntegerField( unique=True)
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.dept_name)

class Programme(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    year_of_admission = models.IntegerField()
    admission_no = models.IntegerField()
    programme_id = models.ForeignKey(Programme, on_delete=models.CASCADE)
    uty_reg_no = models.CharField(max_length=50, primary_key = True)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)

class Item(models.Model):
    item_id = models.IntegerField( unique=True)
    item_name = models.CharField(max_length=50)
    ITEM_TYPE = [
         ('SPORTS', 'SPORTS'),
         ('ATHLETICS', 'ATHLETICS'),
    ]
    item_type = models.CharField(max_length=50,  choices=ITEM_TYPE, default='Active')
    no_of_players = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return str(self.item_name)

class Stud_item(models.Model):
    item_id = models.ManyToManyField(Item)
    PLAYER_STATUS_CHOICES = [
         ('Active', 'Active'),
         ('Inactive', 'inactive'),
    ]
    player_status = models.CharField(max_length=10, choices=PLAYER_STATUS_CHOICES, default='Active')
    UTY_SELECTION_STATUS_CHOICES = [
        ('selected', 'selected'),
         ('not selected', 'not selected'),
    ]
    uty_team_selection = models.CharField(max_length=20, choices=UTY_SELECTION_STATUS_CHOICES, default='Active')




#class Department(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Sport(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Player(models.Model):
#     sl_no = models.AutoField(primary_key=True)
#     stud_name = models.CharField(max_length=100)
#     stud_id = models.CharField(max_length=20, unique=True)  # Assuming stud_id is a unique identifier
#     sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     dob = models.DateField()
#     year = models.IntegerField()
#     place = models.CharField(max_length=100)
#     PLAYER_STATUS_CHOICES = [
#         ('Active', 'Active'),
#         ('Inactive', 'Inactive'),
#     ]
#     player_status = models.CharField(max_length=10, choices=PLAYER_STATUS_CHOICES, default='Active')
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Other', 'Other'),
#     ]
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     position = models.IntegerField()
#     selected_to_university = models.BooleanField(default=False)
#     graduation_level = models.CharField(max_length=50)

#     def __str__(self):
#         return self.stud_name
