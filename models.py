from django.db import models
from django.core.urlresolvers import reverse

class University(models.Model):
    uni_name = models.CharField(max_length=1000, unique=True)
    uni_slug = models.SlugField(max_length=200,
                                db_index=True,
                                unique=True)

    def __str__(self):
        return self.uni_name

    def get_absolute_url(self):
        return reverse('komp:trainprog_list',
                        args=[self.uni_slug])


class TrainingPrograms(models.Model):
    prog_name = models.CharField(max_length=200,
                                 unique=True)
    prog_cod = models.CharField(max_length=10,
                                unique=True)
    prog_uni = models.ForeignKey('University',
                                 on_delete=models.CASCADE,)
    prog_slug = models.SlugField(max_length=200,
                                 db_index=True,
                                 unique=True)

    def __str__(self):
        return self.prog_name

    def get_absolute_url(self):
        return reverse('komp:course_list',
                        args=[self.id])

class Course(models.Model):
    cours_name = models.CharField(max_length=200, unique=True)
    cours_about = models.TextField()
    cours_train = models.ForeignKey('TrainingPrograms',
                                    on_delete=models.CASCADE,)
    cours_slug = models.SlugField(max_length=200,
                                  db_index=True,
                                  unique=True)

    def __str__(self):
        return self.cours_name


class PredCourse(models.Model):
    pred_cours = models.ForeignKey('Course', related_name='predcourse_coursename')
    pred_prcours = models.ManyToManyField('Course', related_name='predcourse_predcours')


class Competence(models.Model):
    comp_cod = models.CharField(max_length=6)
    comp_about = models.TextField()
    comp_tarin = models.ForeignKey('TrainingPrograms',
                                   on_delete=models.CASCADE,)
    comp_course = models.ForeignKey('Course',
                                    on_delete=models.CASCADE,)

    def __str__(self):
        return self.comp_cod
