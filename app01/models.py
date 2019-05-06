from django.db import models

# Create your models here.

class Classes(models.Model):
    '''
    班级表
    '''
    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")


class Teachers(models.Model):

    '''
    老师表
    '''
    name = models.CharField(max_length=32)

# class CT(models.Model):
#
#     c = models.ForeignKey(Classes)
#     t = models.ForeignKey(Teachers)
class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    sex = models.NullBooleanField()#可以为空的布尔值
    cs = models.ForeignKey(Classes,on_delete=models.CASCADE)