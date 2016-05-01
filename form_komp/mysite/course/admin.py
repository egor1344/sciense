from django.contrib import admin
from .models import Course, PredCourse, Competence


class PredCourseLine(admin.StackedInline):
    model = PredCourse
    filter_horizontal = ('prcours',)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra
        return extra


class CompetenceLine(admin.StackedInline):
    model = Competence

    # def get_extra(self, request, obj=None, **kwargs):
    #     extra = 1
    #     if obj:
    #         return extra
    #     return extra


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'tr']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        PredCourseLine,
    ]
admin.site.register(Course, CourseAdmin)


class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('cod', 'about', 'tr')
    filter_horizontal = ('course',)
admin.site.register(Competence, CompetenceAdmin)


class PredCourseAdmin(admin.ModelAdmin):
    list_display = ['cours']
    filter_horizontal = ('prcours',)
admin.site.register(PredCourse, PredCourseAdmin)
