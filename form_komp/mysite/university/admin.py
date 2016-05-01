from django.contrib import admin
from .models import TrainingPrograms, University


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name_s','name_f')
    prepopulated_fields = {'slug': ('name_s',)}

class TrainingProgramsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'cod', 'uni']

admin.site.register(University, UniversityAdmin)
admin.site.register(TrainingPrograms, TrainingProgramsAdmin)
