from django.db import models
from university.models import TrainingPrograms

class Course(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    about = models.TextField(blank=True)
    tr = models.ForeignKey(TrainingPrograms)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return self.name


class PredCourse(models.Model):
    cours = models.ForeignKey('Course',
                              related_name='pr_cours')
    prcours = models.ManyToManyField('Course',
                                     related_name='pr_predcours',
                                     blank=True)


class Competence(models.Model):
    cod = models.CharField(max_length=6)
    about = models.TextField()
    tr = models.ForeignKey(TrainingPrograms)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return self.cod
