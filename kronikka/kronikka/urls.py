from django.conf.urls import patterns, url
from .views import index, student_stories, new_student_story

urlpatterns = patterns(
    '',
    url(
        regex='^$',
        view=index,
        name="index",
    ),
    url(
        regex='^student/(?P<student_id>\d+)/$',
        view=student_stories,
        name="student",
    ),
    url(
        regex='^student/(?P<student_id>\d+)/new_story/$',
        view=new_student_story,
        name="new_story"
    )
)
