from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.course_name


class CustomUser(AbstractUser):
    course_assigned = models.ManyToManyField(CourseModel,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)


class TopicsModel(models.Model):
    course_name = models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)
    topic_url = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    update_date = models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):
        return f'{self.course_name} {self.topic_name}'