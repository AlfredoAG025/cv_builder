from django.db import models

class SocialLink(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='social_links')
    description = models.CharField(max_length=255)
    link = models.URLField()

class Resume(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    address_1 = models.TextField()
    address_2 = models.TextField()
    phone = models.CharField(max_length=30)

class ProfessionalExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='professional_experiences')
    position_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    work_summary = models.TextField()

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    school_location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    description = models.TextField()

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=200)
