from django.shortcuts import render, get_object_or_404
from .models import Student, Story
from django.db.models import Count


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
    student = get_object_or_404(Student, pk=student_id)
    stories = Story.objects.filter(student=student)
    return render(request, "student.html", {
        "student": student,
        "stories": stories,
    })
