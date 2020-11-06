from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import os

# Create your views here.
from .models import *


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        # 获取请求参数
        uname = request.POST.get('uname', '')
        photo = request.FILES.get('photo', '')
        print(photo)
        if not os.path.exists('media'):
            os.makedirs('media')
        with open(os.path.join(os.getcwd(), 'media', photo.name), 'wb') as fw:
            # photo.read()一次性读取文件到内存
            # fw.write(photo.read())
            # 分块读取 photo.chunks()
            for ck in photo.chunks():
                fw.write(ck)
        return HttpResponse('上传成功')
    else:
        return HttpResponse('当前访问量过大请稍后再试')


# django文件上传
def upload_view(request):
    # 接收请求参数
    uname = request.POST.get('uname', '')
    photo = request.FILES.get('photo', '')
    # 入库操作
    Student.objects.create(sname=uname, photo=photo)

    return HttpResponse('上传成功！')


# 显示图片
def showall_view(request):
    # 读取所有学生信息
    stus = Student.objects.all()

    return render(request, 'show.html', {'stus': stus})


def download_view(request):
    # 获取请求参数（图片存储位置）
    photo = request.GET.get('photo', '').replace('/', '\\')
    # 获取图片文件名
    filename = photo[photo.rindex('\\') + 1:]
    # 开启一个流
    import os
    path = os.path.join(os.getcwd(), 'media', photo)
    with open(path, 'rb') as fr:
        response = HttpResponse(fr.read())
        response['Content-Type'] = 'image/png'
        response['Content-Disposition'] = 'attachment;filename=' + filename
    return response


def index_view2(request):
    return redirect('/student/showallRedirect/')


def showallRedirect_view(request):
    return HttpResponse('hello')
