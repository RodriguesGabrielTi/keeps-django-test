from rest_framework import viewsets

from student.models import Student
from student.serializers.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Student.objects.filter()

    def get_serializer_class(self):
        return StudentSerializer
