import uuid

from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Name', max_length=200)
    nick_name = models.CharField(verbose_name='Nick Name', max_length=400)
    phone = models.CharField(verbose_name='Phone', max_length=400, null=True, blank=True)
    avatar = models.URLField(verbose_name='Avatar', null=True, blank=True)

    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    class Meta:
        verbose_name_plural = "Student"
        db_table = "student"
