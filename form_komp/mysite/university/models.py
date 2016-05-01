from django.db import models
from django.core.urlresolvers import reverse


class University(models.Model):
    name_s = models.CharField(max_length=20,
                              db_index=True,
                              unique=True)
    name_f = models.TextField()
    about = models.TextField()
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name_s

    def get_absolute_url(self):
        return reverse('university:trprog_list',
                       args=[self.slug])


class TrainingPrograms(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    cod = models.CharField(max_length=10)
    about = models.TextField()
    uni = models.ForeignKey('University',
                            on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name
