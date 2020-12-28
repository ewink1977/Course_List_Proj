from django.db import models
from django.db.models.deletion import CASCADE

class Courses(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Descriptions(models.Model):
    desc = models.TextField()
    course = models.ForeignKey(Courses, related_name="description", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    course_comment = models.ForeignKey(Courses, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

