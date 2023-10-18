from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
#python manage.py runserver可看網址
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals()) 
    #傳給index.html locals把變數集合(後端)

def showpost(request,slug):
    try: 
        post=Post.objects.get(slug=slug) #看網站選到哪裡傳到slug變數
        if post != None: #post是超連結之後連到的網站
            return render(request,'post.html',locals())
        else:
            return redirect("/") #導到首頁
    except:
        return redirect("/") #redirect轉址
'''
def homepage(requset):  #網站設參數給view
    posts=Post.objects.all() 
    posts_list=list()
    for counter,post in enumerate(posts):
        posts_list.append(f'No. {counter}-{post} <br>') #br是換行
    return HttpResponse(posts_list)  
'''