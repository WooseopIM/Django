from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from IPython import embed
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.

def signup(request):
    if request.user.is_authenticated: # 이미 로그인이 되어 있니?
        return redirect('movies:index')
    if request.method == "POST":
        # 클래스 인스턴스 선언
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 유효하면 실제 DB에 정보 저장
            form.save()
            return redirect('movies:index')
    else:
        # GET 요청일때는 아래 과정
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated: # 이미 로그인이 되어 있니?
        return redirect('movies:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효하면 로그인 시켜!
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

def logout(request):
    # 세션(에서 로그인 정보) 지우기
    auth_logout(request)
    return redirect('movies:index')

@require_POST
def delete(request):
    # DB에서 User를 삭제한다.
    '''
    user = User.objects.get(pk=request.user.pk)
    user.delete()

    위의 두 줄이 아래의 한 줄로

    request.user.delete()
    '''
    request.user.delete()
    return redirect('movies:index')

@login_required
def update(request):
    if request.method == "POST":
        # 실제 DB에 적용
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        # 편집 화면 보여줌
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form':form
        }
        return render(request, 'accounts/auth_form.html', context)


def change_password(request):
    if request.method == "POST":
        # 실제 password 변경
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # session auth hash가 변경되어 비밀번호 수정하고나면 session이 끝나서 로그아웃이 되어버림. 이를 수정하기 위해서 아래 코드 써주기
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        # 편집 화면 보여줌
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/auth_form.html',context)

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    user = request.user
    
    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('profile', person.username)