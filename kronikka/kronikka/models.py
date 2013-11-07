from django.db import models


class Tutor(models.Model):
    """Students belong to a Tutor group"""
    name = models.CharField(max_length=30)
    organization = models.CharField(
        max_length=2,
        choices=(
            ('as', 'Asteriski'), ('di', 'Digit')
        )
    )

    def __unicode__(self):
        return self.name

    def get_students(self):
        return Student.objects.filter(tutor=self)


class Student(models.Model):
    """ Django model for the student """
    name = models.CharField(max_length=30)
    thumbnail = models.ImageField(upload_to="thumbnails/",
                                  default="thumbnails/nic_cage.jpg")
    tutor = models.ForeignKey(Tutor)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    """ An user submitted story about a student """
    student = models.ForeignKey(Student)
    story = models.TextField()
