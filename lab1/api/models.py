
from django.db import models
from django.utils.timezone import now


# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=now, blank=True)


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gpa = models.FloatField(default=0.0, blank=True, null=False)
    klass = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Name: {}\n'.format(self.name)

