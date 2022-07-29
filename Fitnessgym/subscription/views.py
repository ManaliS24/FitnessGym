from django.shortcuts import render, redirect
from gym.models import Course
from .models import Plan
from django.views import generic
from .forms import PlanMembersForm, CourseMembersForm
# Create your views here.


def register(request, name, type):
    # courses=Course.objects.all()
    if type == 'plan':
        print(" Registration type is plan.")
        # load form with inital dropdown value selected
        # plans = Plan.objects.all()
        # plan_list = list(plans)
        # # index=0;
        # for plan in plan_list:
        #     if str(plan).startswith(name):
        #         break

        plan = Plan.objects.filter(name__startswith=name).first()
        print(plan)
        # form = PlanMembersForm(initial={'plan_name': plan})
        form = PlanMembersForm(initial={'plan_name': plan})
        if request.method == 'POST':
            print("request method is post.")
            form = PlanMembersForm(request.POST)
            print("PlanMemberform is created.")
            if form.is_valid():
                print("form is validated.")
                # save the data
                form.save()
                return redirect('index')
    else :
        print("Registration type is course.")
        course = Course.objects.filter(name__startswith=name).first()
        print(course)
        form = CourseMembersForm(initial={'course_name': course})
        if request.method == 'POST':
            print("request method is post.")
            form = CourseMembersForm(request.POST)
            print("CourseMemberform is created.")
            if form.is_valid():
                print("form is validated.")
                # save the data
                form.save()
                return redirect('index')


    # if type == 'plan':
    #     form = PlanMembersForm()


    context ={
        'form':form,
        'name': name,
        'type': type,
        # 'courses': courses,
        # 'plans': plans
    }
    return render(request, "registrationform.html", context)

# def registration(request, name, type):
    # courses=Course.objects.all()
    # plans=Plan.objects.all()
    # return render(request, "registrationform.html",{'name':name, 'type':type,'courses':courses, 'plans':plans})



