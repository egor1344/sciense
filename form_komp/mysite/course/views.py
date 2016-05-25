# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Course, PredCourse, Competence
from django.core.exceptions import ObjectDoesNotExist
from openpyxl import Workbook
from django.http import HttpResponse


def form_komp(course=None):
    list_comp = Competence.objects.filter(tr=course.tr)\
                                  .filter(course=course)
    pred_list = PredCourse.objects.all().filter(cours=course)
    try:
        pred_list = pred_list[0].prcours.all()
    except ObjectDoesNotExist:
        pred_list = []
    except IndexError:
        pred_list = []
    predcomp_list = {}
    for pred in pred_list:
        predcomp_list[pred] = Competence.objects.filter(tr=course.tr)\
                                                .filter(course__slug=pred.slug)
    return list_comp, predcomp_list

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
    comp_list, predcomp_list = form_komp(course)
    return render(request,
                  "course/list/course_detail.html",
                  {'comp_list': comp_list,
                   'course': course,
                   'predcomp_list': predcomp_list})

def course_xlsx(request, slug, slug_c):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Course.xlsx"'

    course = Course.objects.get(slug=slug_c)
    list_comp, predcomp_list = form_komp(course)
    wb = Workbook()
    ws = wb.active
    ws.append(['Название дисциплины', course.name ])
    ws.append([])
    if predcomp_list:
        ws.append(['Входящие компетенции'])
        ws.append(["Код","Описание","Предшествующая дисциплина"])
        for pred, comp_list in predcomp_list.items():
            for comp in comp_list:
                ws.append([comp.cod,comp.about,pred.name])
    else:
        ws.append(['Входящих компетенций нет'])
    ws.append([])

    if list_comp:
        ws.append(['Исходящие компетенции'])
        ws.append(["Код","Описание"])
        for comp in list_comp:
            ws.append([comp.cod, comp.about])
    else:
        ws.append(['Исходящих компетенций нет'])

    wb.save(response)
    return response