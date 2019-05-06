from django.shortcuts import render,redirect
from app01 import models

def get_classes(request):
    cls_list = models.Classes.objects.all()
    return render(request,"get_classes.html",{'cls_list':cls_list})

def add_classes(request):
    if request.method == "GET":
        return render(request,"add_classes.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        models.Classes.objects.create(title=title)
        return redirect("/classes")

def del_classes(request):


   nid = request.GET.get("nid")
   models.Classes.objects.filter(id=nid).delete()
   return redirect("/classes")

def edit_classes(request):
    if request.method == "GET":
        nid = request.GET.get("nid")
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request,"edit_classes.html",{"obj":obj})
    elif request.method == "POST":
        nid = request.GET.get("nid")
        title = request.POST.get("title")
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes')


def set_teachers(request):
        if request.method == 'GET':
            nid = request.GET.get('nid')
            cls_obj = models.Classes.objects.filter(id=nid).first()
            cls_teacher_list = cls_obj.m.all().values_list('id','name')
            #当前班级任课教师列表
            id_list = list(zip(*cls_teacher_list))[0] if list(zip(*cls_teacher_list)) else []

            all_teachers_list = models.Teachers.objects.all()
            return render(request,"set_teachers.html",
                        {
                            'id_list':id_list,
                            'all_teachers_list':all_teachers_list,
                            'nid':nid

                        }
            )
        elif request.method == "POST":

            nid = request.GET.get('nid')
            teacher_ids = request.POST.getlist('teacher_ids')
            models.Classes.objects.filter(id=nid).first().m.set(teacher_ids)
            return redirect('/classes')