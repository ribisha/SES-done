from django.contrib import admin
from .models import *

@admin.register(StudentApplication)
class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = StudentApplication.DisplayFields
    search_fields = StudentApplication.SearchableFields

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'time', 'is_read')
    list_filter = ('is_read',)
    actions = ['mark_as_read']

    def student_name(self, obj):
        return obj.student.student_name
    
    student_name.short_description = 'Student Name'

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    mark_as_read.short_description = 'Mark selected notifications as read'