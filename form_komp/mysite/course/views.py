from django.shortcuts import render
from .models import Course, PredCourse, Competence
from django.core.exceptions import ObjectDoesNotExist


def course_list(request, slug):
    c_list = Course.objects.filter(tr__slug=slug)
    return render(request,
                  "course/list/course_list.html",
                  {'c_list': c_list})


def course_detail(request, slug, slug_c):
    """
        Всю эту хуйню переделать
    """
    course = Course.objects.get(slug=slug_c)
    comp_list = Competence.objects.filter(tr__slug=slug)\
                                  .filter(course__slug=slug_c)
    pred_list = PredCourse.objects.all().filter(cours__slug=slug_c)
    try:
        pred_list = pred_list[0].prcours.all()
    except ObjectDoesNotExist:
        pred_list = []
    except IndexError:
        pred_list = []
    predcomp_list = {}
    for pred in pred_list:
        predcomp_list[pred] = Competence.objects.filter(tr__slug=slug)\
            .filter(course__slug=pred.slug)
    return render(request,
                  "course/list/course_detail.html",
                  {'comp_list': comp_list,
                   'course': course,
                   'predcomp_list': predcomp_list})
