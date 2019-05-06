from django.shortcuts import render,redirect
from app01 import models


def get_students(request):
    stu_list = models.Student.objects.all()
    cs_list = models.Classes.objects.all()

    return render(request,"get_students.html",{"stu_list":stu_list,"cs_list":cs_list})


def add_students(request):
    if request.method == "GET":
        # models.Student.objects.create()
        cs_list = models.Classes.objects.all()
        return render(request,"add_students.html",{"cs_list":cs_list})
    elif request.method == "POST":
        username = request.POST.get("username")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        cs = request.POST.get("cs")
        models.Student.objects.create(
            username=username,
            age=age,
            sex=gender,
            cs_id=cs
        )
        return redirect('/students')

def del_students(request):

    sid = request.GET.get("sid")
    models.Student.objects.filter(id=sid).delete()

    return redirect('/students')

def edit_students(request):
    if request.method == "GET":
        sid = request.GET.get("sid")
        obj = models.Student.objects.filter(id=sid).first()
        print(obj.sex)
        cs_list = models.Classes.objects.all()
        return render(request,"edit_students.html",locals())
    elif request.method == "POST":
        sid = request.GET.get("sid")
        username = request.POST.get("username")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        cs = request.POST.get("cs")
        models.Student.objects.filter(id=sid).update(username=username,age=age,sex=gender,cs=cs)

        return redirect('/students')