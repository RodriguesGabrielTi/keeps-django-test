import uuid

from django.db import models


# Create your models here.
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Name', max_length=200)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    holder_image = models.URLField(verbose_name='Holder Image', null=True, blank=True)
    duration = models.IntegerField(verbose_name='Duration', default=0)

    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    class Meta:
        verbose_name_plural = "Courses"
        db_table = "course"
