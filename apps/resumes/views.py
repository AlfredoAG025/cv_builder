from django.shortcuts import render

from apps.resumes.forms import ResumeForm

def create_cv(request):
    form = ResumeForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/resumes/create.html', context)
