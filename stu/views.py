from django.http import HttpResponse
from django.shortcuts import render
import os


# Create your views here.
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
