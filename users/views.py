from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout 

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            auth_user = authenticate(request,username=username,password=password)
            if auth_user is not None:
                auth_login(request,auth_user)
                return redirect('blog:index')
    # 단순히 로그인 페이지에 접속했을경우
    else:
        form = forms.LoginForm()

    return render(request,'users/login.html',{'form':form})

def logout(request):
    auto_logout(request)
    return redirect('blog:index')
    

def signup(request):
    # 회원가입 정보를 입력폼에 작성하고, 제출버튼을 눌렀을경우
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        # 입력폼의 내용이 유효한경우
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            # 입력폼에서 입력받은 username, email, password를 토대로 계정을 하나 새로 생성
            user = User.objects.create_user(username=username,email=email,password=password)
            # 위의 login 함수에서 정의했던 내용과 동일하게, 밑으로는 로그인하는 과정이 나타나있음
            auth_user = authenticate(request,username=username,password=password)
            if auth_user is not None:
                auth_login(request,auth_user)
                return redirect('blog:index')
    # 단순히 회원가입 페이지에 접속했을경우
    else:
        form = forms.SignUpForm()
    return render(request,'users/signup.html',{'form':form})