
from django.views import generic
from django.shortcuts import render
from .models import Trainer, Course, TimeTable
from subscription.models import Plan
from datetime import datetime, timedelta
# Create your views here.


def index(request):
    plan = Plan.objects.all()
    course = Course.objects.all()
    trainer = Trainer.objects.all()

    today = datetime.now()
    if today.hour > 18:
        today = today + timedelta(days=1)

    tomorrow = today + timedelta(days=1)
    next_classes_1 = TimeTable.objects.select_related('course').filter(day_of_week=today.strftime('%A'))
    next_classes_2 = TimeTable.objects.select_related('course').filter(day_of_week=tomorrow.strftime('%A'))

    return render(request, "index.html", {'trainers': trainer, 'plans': plan, 'courses': course, 'next_classes_1': next_classes_1,'next_classes_2': next_classes_2})


def about(request):
    return render(request, "about.html")


def trainer(request):
    courses = Course.objects.select_related('trainer')
    return render(request, "trainers.html", {'courses': courses})


def classes(request):
    courses = Course.objects.all()
    course_list = Course.objects.select_related('trainer')
    print(course_list.query)
    print(courses.query)
    return render(request, "classes.html", {"course_list": course_list,
                                     "courses": courses} )


# class CourseView(generic.ListView):
#     template_name = 'classes.html'
#     context_object_name = 'course'
#
#     def get_queryset(self):
#         course = Course.objects.select_related('trainer')
#         print(course.query)
#         return course


class NewCourseView(generic.DetailView):
    model = Trainer
    template_name = 'class.html'


def timetable(request):
    plan = Plan.objects.all()
    course = Course.objects.all()
    trainer = Trainer.objects.all()
    timetable = TimeTable.objects.all()

    today = datetime.now()
    if today.hour > 18:
        today = today + timedelta(days=1)

    next_classes = TimeTable.objects.select_related('course').filter(day_of_week=today.strftime('%A'))


    return render(request, "timetable.html", {'timetable': timetable,
                                          'courses': course,
                                          'trainers': trainer,
                                          'next_classes': next_classes})


def trainerprofile(request, *args, **kwargs):
    name= kwargs['name']
    trainer=Trainer.objects.get(name__exact=name)
    return render(request, "trainersprofile.html", {'trainer': trainer})


class TrainerProfile(generic.DetailView):
    model = Trainer
    template_name = 'trainerprofile.html'


    def get_queryset(self,*args, **kwargs):
        print(args)
        trainer=Trainer.objects.filter(name__startwith="Ratna")

        return trainer



def blog(request):
    pass


def pricing(request):
    plans=Plan.objects.all()
    courses=Course.objects.all()

    return render(request,"pricing.html", {'plans':plans,
                                           'courses':courses})


def contact(request):
    return render(request, "contact.html")