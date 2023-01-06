
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('aboutContent/', views.aboutContent, name="aboutContent"),
    path('education/', views.education, name="education"),
    path('workExp/', views.workExp, name="workExperience"),
    path('skills/', views.skills, name="skills"),
    path('achievements/', views.achievements, name="achievements"),
]
