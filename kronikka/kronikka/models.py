from django.db import models


class Student(models.Model):
    """ Django model for the student """
    name = models.CharField(max_length=30)
    thumbnail = models.ImageField()


class Tutor(models.Model):
    """Students belong to a Tutor group"""
    name = models.CharField(max_length=30)
    organization = models.CharField(
        max_length=2,
        choices=(
            ('as', 'Asteriski'), ('di', 'Digit')
        )
    )


class Story(models.Model):
    """ An user submitted story about a student """
    student = models.ForeignKey(Student)
    story = models.TextField()
