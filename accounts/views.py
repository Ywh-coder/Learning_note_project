from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """新用户注册"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #用户自动登录，重定向到主页
            login(request, new_user)
            return redirect('learning_notes:index')
    context = {'form':form}
    return render(request,'registration/register.html',context)
