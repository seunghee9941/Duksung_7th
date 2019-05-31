from django.db import models

# Create your models here.

class Apply(models.Model):
    name = models.CharField(max_length=30,null=False, default='')
    major = models.CharField(max_length=30,null=False, default='')
    student_id = models.IntegerField(null=False, default='')
    email = models.EmailField(null=False, default='')
    phone = models.IntegerField(null=False, default='')
    body = models.TextField(null=False, default='')
    file = models.FileField(upload_to='upload',null=False, default='')
    isFinal = models.BooleanField(default=False)