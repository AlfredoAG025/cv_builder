from django.urls import path

from apps.resumes.views import resume_create, resume_preview

app_name = 'resumes'

urlpatterns = [
    path('editor/', resume_create, name='create'),
    path('preview/', resume_preview, name='preview'),
]
