from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def secondpage(request):
    return render(request, 'main/secondpage.html')

def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {  
            'date' : '2026.04.01',                         
            'topic': 'Django',
            'week': '1학기 2주차',
            'instructor': '백엔드 교육팀 11기 차은호'
        },
        'shortcuts': [
            'Django_Project : 하나의 서비스 전체를 의미',
            'Django_App : Project를 구성하는 기능의 집합 단위',
            '첫 페이지 생성: HTML/VIEW/URL 작성 ',
            'Template 언어: URL 연결 / 변수 사용 / 반복문',
            '-> 크게 URL 연결, 변수 사용, 반복문, 조건문, 필터 기능 지원!',     
            '중복되는 html 파일 정리: template 상속 / navbar 분리',          
            '정적 파일 분리: css 분리 / image 분리'
        ]
    }
    return render(request, 'main/mainpage.html', context)

def new_post(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'main/new_post.html')

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    new_post = Post()
    
    new_post.title = request.POST['title']
    new_post.writer = request.user.username
    new_post.pub_date = request.POST['pub_date']
    new_post.content = request.POST['content']
    new_post.category = request.POST['category']
    
    new_post.save()
    
    return redirect('main:detail', new_post.id)

def postpage(request):
    posts = Post.objects.all()
    return render(request, 'main/postpage.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/detail.html', {'post':post})

def edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    edit_post = get_object_or_404(Post, pk=post_id)
    
    if edit_post.writer != request.user.username:
        return redirect('main:detail', edit_post.id)
    
    return render(request, 'main/edit.html', {"post":edit_post})

def update(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    update_post = get_object_or_404(Post, pk=post_id)
    
    if update_post.writer != request.user.username:
        return redirect('mian:detail', update_post.id)
    
    update_post.title = request.POST['title']
    update_post.writer = request.user.username
    update_post.pub_date = request.POST['pub_date']
    update_post.content = request.POST['content']
    update_post.category = request.POST['category']
    update_post.save()
    
    return redirect('main:detail', update_post.id)

def delete(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    delete_post = get_object_or_404(Post, pk=post_id)
    
    if delete_post.writer != request.user.username:
        return redirect('main:detail', delete_post.id)
    
    delete_post.delete()
    
    return redirect('main:postpage')