from django.shortcuts import render

from apps.resumes.forms import ResumeForm

def resume_create(request):
    form = ResumeForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect("resume-list")

    return render(request, "apps/resumes/create.html", {"form": form})

def resume_preview(request):
    form = ResumeForm(request.POST)

    if form.is_valid():
        resume = form.cleaned_data
    else:
        resume = {}

    return render(
        request,
        "apps/resumes/preview.html",
        {"resume": resume}
    )