from django.db import models
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)  # Gold, Platinum, Diamond
    img = models.ImageField(upload_to='pics', blank=True, null=True)
    desc = models.TextField(max_length=100)
    price = models.IntegerField()
    discount = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Trainer(models.Model):
    name = models. CharField(max_length= 50)
    img = models.ImageField(upload_to='pics', blank=True, null=True)
    desc = models.TextField(max_length=1000)
    course = models.OneToOneField(Course, on_delete=models.SET_NULL, default='', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class TimeTable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True,blank=True)
    day_of_week = models.CharField(max_length=10)
    start_end_time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}={self.day_of_week}-{self.start_end_time}"


