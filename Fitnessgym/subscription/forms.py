import django.forms as forms
from django.forms import ModelForm,widgets
from .models import *


class PlanMembersForm(ModelForm):

    class Meta:
        model = PlanMembers
        fields = "__all__"
        GENDER_CHOICE = [('M', 'Male'),('F', 'Female')]

        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'date'}),
            'phone': forms.TextInput(attrs={'type': 'phoneNumber', 'class': 'form-control'}),
            # 'plan_name': forms.ModelChoiceField(queryset=Plan.objects.all().order_by('name')),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=GENDER_CHOICE, attrs={'class': 'radio-inline','type':'radio'})
        }

    def __init__(self, *args, **kwargs):
        super(PlanMembersForm, self).__init__(*args, **kwargs)
        # self.fields['date_of_birth'].widget = forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'})
        # self.fields['gender'].widget=forms.ChoiceField(choices=('M','F'),)


class CourseMembersForm(ModelForm):

    class Meta:
        model = CourseMembers
        fields = "__all__"
        GENDER_CHOICE = [('M', 'Male'),('F', 'Female')]

        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'date'}),
            'phone': forms.TextInput(attrs={'type': 'phoneNumber', 'class': 'form-control'}),
            # 'plan_name': forms.ModelChoiceField(queryset=Plan.objects.all().order_by('name')),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=GENDER_CHOICE, attrs={'class': 'radio-inline','type':'radio'})
        }

    def __init__(self, *args, **kwargs):
        super(CourseMembersForm, self).__init__(*args, **kwargs)
        # self.fields['date_of_birth'].widget = forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'})
        # self.fields['gender'].widget=forms.ChoiceField(choices=('M','F'),)