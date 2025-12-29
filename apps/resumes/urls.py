from django.urls import path

from apps.resumes.views import create_cv

app_name = 'resumes'

urlpatterns = [
    path('editor/', create_cv, name='create'),
    path('preview/', create_cv, name='resume_preview'),
]
