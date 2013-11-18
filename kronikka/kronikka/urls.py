from django.conf.urls import patterns, url
from .views import index, student_stories

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
)
