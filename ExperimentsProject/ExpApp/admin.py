from django.contrib import admin
from .models import CustomUser,CourseModel,TopicsModel
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser,UserAdmin)


@admin.register(CourseModel)
class AdminCourse(admin.ModelAdmin):
    list_display=['course_name']


@admin.register(TopicsModel)
class AdminTopics(admin.ModelAdmin):
    list_display=['course_name','topic_name']

