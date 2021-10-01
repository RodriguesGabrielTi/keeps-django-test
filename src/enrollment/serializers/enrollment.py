from rest_framework import serializers

from enrollment.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    class meta:
        model = Enrollment
        depth = 2
        fields = '__all__'

