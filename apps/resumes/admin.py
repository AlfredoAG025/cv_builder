from django.contrib import admin

from apps.resumes.models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass
