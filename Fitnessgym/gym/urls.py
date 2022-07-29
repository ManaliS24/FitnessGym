"""Fitnessgym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('trainers/', views.trainer, name="trainers"),
    # path('trainers/<str>', views.TrainerProfile.as_view(), name="trainerprofile"),
    path('trainers/<str:name>', views.trainerprofile, name="trainerprofile"),
    path('classes/', views.classes, name="classes"),
    # path('classes/<int:pk>', views.NewCourseView.as_view(), name="classes"),
    path('timetable/', views.timetable, name="timetable"),
    path('pricing/', views.pricing, name="pricing"),
    path('contact/', views.contact, name='contact')
]

#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
