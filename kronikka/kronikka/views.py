from django.shortcuts import render
from .models import Student


def index(request):
    """
    View showing all the tutors and their students
    if GET-attribute "name" exists then filter the results accoringly
    """
    students = Student.objects.select_related().all().order_by("tutor")
    if request.GET.get("name"):
        student_name = request.GET.get("name")
        students = students.filter(name__contains=student_name)
    return render(request, "base.html", {
        "students": students,
    })
