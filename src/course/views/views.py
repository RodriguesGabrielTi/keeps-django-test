from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from course.models import Course
from course.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Course.objects.filter()

    serializer_class = CourseSerializer

