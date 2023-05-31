from django.contrib import admin

from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from core.models import Subject, SubjectRecord, Major, Place

# Register your models here.


@admin.register(Subject)
class SubjectAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    model = Subject
    list_display = ['name', 'rank', 'organization_id', 'serve_place']
    search_fields = ['name', 'rank', 'organization_id',
                     'national_id', 'skills', 'education_field']
    autocomplete_fields = ['major']

    # @admin.display(description='محل خدمت', ordering='created')
    # def serve_place(self, obj: Subject):
    #     return SubjectRecord.objects.filter(subject=obj).order_by('-created_at').values_list('subject_place').first().name

    # @admin.display(description='درجه', ordering='created')
    # def rank(self, obj: Subject):
    #     return SubjectRecord.objects.filter(subject=self).order_by('-created_at').first().get_subject_rank_display()

    @admin.display(description='نام و نشان', ordering='created')
    def name(self, obj: Subject):
        return f'{obj.first_name} {obj.last_name}'


@admin.register(SubjectRecord)
class SkillModelAdmin(admin.ModelAdmin):
    model = SubjectRecord
    autocomplete_fields = ['subject']


@admin.register(Major, Place)
class BaseAdmin(admin.ModelAdmin):
    search_fields = ['name']
