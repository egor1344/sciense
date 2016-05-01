from django.contrib import admin
from .models import Competence, PredCourse, Course, TrainingPrograms, University


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('uni_name',)
    prepopulated_fields = {'uni_slug': ('uni_name',)}


class CompetenceLine(admin.TabularInline):
    model = Competence
    raw_id_fields = ("comp_tarin", "comp_course",)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra
        return extra


class CourseAmin(admin.ModelAdmin):
    inlines = [
        CompetenceLine,
    ]
    list_display = ['cours_name', 'cours_train']
    prepopulated_fields = {'cours_slug': ('cours_name',)}


class TrainingProgramsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'prog_slug': ('prog_name',)}
    list_display = ['prog_name', 'prog_cod', 'prog_uni']


class PredCourseAdmin(admin.ModelAdmin):
    list_display = ['pred_cours']
    filter_horizontal = ('pred_prcours',)

admin.site.register(Competence)
admin.site.register(University, UniversityAdmin)
admin.site.register(TrainingPrograms, TrainingProgramsAdmin)
admin.site.register(Course, CourseAmin)
admin.site.register(PredCourse, PredCourseAdmin)