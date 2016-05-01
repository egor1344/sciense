from django.shortcuts import render
from .models import TrainingPrograms, University


def university_list(request):
    uni_list = University.objects.all()
    return render(request,
                  "university/list/uni.html",
                  {'uni_list': uni_list})


def trprog_list(request, slug):
    uni = University.objects.get(slug=slug)
    tp_list = TrainingPrograms.objects.filter(uni=uni)
    return render(request,
                  "university/list/tp.html",
                  {'tp_list': tp_list,
                   'uni': uni})
