from django.db import models
from django.core.urlresolvers import reverse


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
                                  default="nic_cage.jpg")
    tutor = models.ForeignKey(Tutor)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kronikka.views.student_stories', args=[str(self.id)])


class Story(models.Model):
    """ An user submitted story about a student """
    student = models.ForeignKey(Student)
    story = models.TextField(verbose_name="Kronikkateksti")

    def __unicode__(self):
        return self.story[:50]

    def get_bootstrap_column_size(self):
        """
        Returns the appropriate column size for bootstrap rendering.
        'col-md-4' if world length is < 20
        'col-md-6' if 20 < 40
        'col-md-12' if > 40
        """
        wc = len(self.story.split())
        if wc < 20:
            return 'col-md-4'
        if wc < 40:
            return 'col-md-6'
        else:
            return 'col-md-12'
