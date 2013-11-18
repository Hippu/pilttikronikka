from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Story
from django.db.models import Count
from .forms import StoryForm


def index(request):
    """
    A view showing all students.
    if GET-attribute "name" exists then filter the results accordingly.
    """
    students = Student.objects.select_related().all().order_by("tutor")
    students = students.annotate(story_count=Count("story"))
    if request.GET.get("name"):
        student_name = request.GET.get("name")
        students = students.filter(name__contains=student_name)
    return render(request, "base.html", {
        "students": students,
    })


def student_stories(request, student_id):
    """
    Shows all the stories written about a student.
    Also display a form for writing new ones.
    """
    student = get_object_or_404(Student, pk=student_id)
    stories = Story.objects.filter(student=student)
    story_form = StoryForm()
    return render(request, "student.html", {
        "form": story_form,
        "student": student,
        "stories": stories,
    })


def new_student_story(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == "POST":
        story = Story(student=student)
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()

    return redirect(student)
