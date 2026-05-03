from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect, render
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main:postpage')
        else:
            return render(request, 'acounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:postpage')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'accounts/signup.html', {
                    'error': '이미 존재하는 아이디입니다.'
                })
            
            newuser = User.objects.create_user(
                username = request.POST['username'],
                password=request.POST['password'],
            )
            
            nickname = request.POST['nickname']
            major = request.POST['major']
            student_id = request.POST['student_id']
            profile_image = request.FILES.get('profile_image')
            
            profile = Profile(
                user=newuser,
                nickname=nickname,
                major=major,
                student_id=student_id,
                profile_image=profile_image,
            )
            profile.save()
            
            auth.login(request, newuser)
            return redirect('main:postpage')
        
    return render(request, 'accounts/signup.html')