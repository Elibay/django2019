from django.urls import path, re_path

from api.views import index, time, multiply, student_detail, students, student_filter

urlpatterns = [
    path('', index),
    path('time/', time),
    path('multiply/<int:a>/<int:b>/', multiply),
    path('student/<int:id>/', student_detail),
    path('students/', students),
    path('filter/<slug:name>/', student_filter),
    # re_path(r'filter/[a-zA-Z]+/', student_filter),
]