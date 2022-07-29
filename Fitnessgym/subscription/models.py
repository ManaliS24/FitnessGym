from django.db import models
from gym.models import Course
from django.core.validators import RegexValidator
# Create your models here.


class Plan(models.Model):
    name = models. CharField(max_length= 10) # Gold, Platinum, Diamond
    img = models.ImageField(upload_to='pics', blank=True, null=True)
    desc = models.TextField(max_length=100)
    price = models.IntegerField()
    discount = models.BooleanField(default =False)

    def __str__(self):
        return f"{self.name}: ${self.price}"


class PlanMembers(models.Model):

    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=10, null=False)  # Gold, Platinum, Diamond
    last_name = models. CharField(max_length= 10) # Gold, Platinum, Diamond
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    date_of_subscription = models.DateTimeField(auto_now_add=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    # phone =models.IntegerField()
    plan_name = models.ForeignKey(Plan, on_delete=models.SET_NULL, default='', blank=True, null=True)
    height=models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE, null=False,default='M')


class CourseMembers(models.Model):
    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=10, null=False)  # Gold, Platinum, Diamond
    last_name = models. CharField(max_length= 10) # Gold, Platinum, Diamond
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    date_of_subscription = models.DateTimeField(auto_now_add=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    # phone =models.IntegerField()
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, default='', blank=True, null=True)
    height=models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE, null=False,default='M')