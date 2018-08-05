from django.db import models

# Create your models here.
from account.models import Gender


# e.g. Bangla, English, Madrasha
class Medium(models.Model):
    name = models.CharField(max_length=20, blank=False)


# e.g. Regular, Irregular, Admission
class Type(models.Model):
    type = models.CharField(max_length=20, blank=True)


# e.g STD 1, 2, O'Levels etc.
class Level(models.Model):
    name = models.CharField(max_length=20, blank=False)


# e.g. class, medium and type of the student
class LevelAttribs(models.Model):
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Student(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    attribs = models.OneToOneField(LevelAttribs, on_delete=models.CASCADE)


class Tuition(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)