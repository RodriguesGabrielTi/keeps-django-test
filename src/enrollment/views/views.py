from rest_framework import viewsets

from enrollment.models import Enrollment
from enrollment.serializers import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Enrollment.objects.filter()

    def get_serializer_class(self):
        return EnrollmentSerializer
