import uuid

from django.db import models

from course.models import Course
from student.models import Student

STATUS = (
        ('APPROVED', 'APPROVED'),
        ('REPROVED', 'REPROVED'),
        ('IN_PROGRESS', 'IN_PROGRESS')
)


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, verbose_name='Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='Student', on_delete=models.CASCADE)
    enroll_date = models.DateTimeField(verbose_name='Enroll Date', null=True)
    close_date = models.DateTimeField(verbose_name='Close Date', null=True)
    score = models.FloatField(verbose_name='Score', null=True, blank=True)
    status = models.CharField(verbose_name='Status', max_length=100, choices=STATUS, null=True, blank=True)

    created_date = models.DateTimeField(verbose_name='Created Date', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Updated Date', auto_now=True)

    class Meta:
        verbose_name_plural = 'Enrollments'
        unique_together = ('student', 'course')
        db_table = 'enrollment'
