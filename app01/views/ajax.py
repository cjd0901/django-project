from django.shortcuts import render,redirect,HttpResponse
import time
from app01 import models


def ajax1(request):

    return render(request,'ajax1.html')


def ajax2(request):
    user = request.GET.get("username")
    pwd = request.GET.get("password")
    time.sleep(5)
    return HttpResponse("小洞洞")

def ajax3(request):

    i1 = request.POST.get("i1")
    i2 = request.POST.get("i2")

    try:
        i3 = int(i1) + int(i2)
    except Exception as e:
        i3 = '输入格式错误'

    return HttpResponse(i3)



def ajax4(request):

    nid = request.GET.get('nid')
    msg = "成功"
    try:
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        msg = str(e)
    return HttpResponse(msg)


def ajax5(request):

    username = request.POST.get("username")
    age = request.POST.get("age")
    sex = request.POST.get("sex")
    cls_id = request.POST.get("cls_id")
    msg = '成功'
    try:
        models.Student.objects.create(
            username=username,
            age=age,
            sex=sex,
            cs_id=cls_id
        )
    except Exception as e:
        msg = "添加学生失败"
    return HttpResponse(msg)

def ajax6(request):
    id = request.POST.get("sid")
    username = request.POST.get("username")
    age = request.POST.get("age")
    sex = request.POST.get("sex")
    cls_id = request.POST.get("cls_id")
    msg = '成功'
    try:
        models.Student.objects.filter(id=id).update(
            username=username,
            age=age,
            sex=sex,
            cs_id=cls_id
        )
    except Exception as e:
        msg = "修改学生失败"
    return HttpResponse(msg)

