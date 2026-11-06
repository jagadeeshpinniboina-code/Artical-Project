from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from userathenciate.form import RegisterForm, UserUpdateForm, ProfileUpdateForm


def logout_page(request):
    logout(request)
    return render(request,'logout.html')

def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST.get('username')
            messages.success(request,f'Account created for {username} successfully!')
            return redirect('login')

        else:
            username=request.POST.get('username')
            messages.warning(request,f'Account was not created for {username}.Please try again!')
            return redirect('register')
    else:
        form=RegisterForm()
        context={
            'form':form
        }
        return render(request,'register.html',context)


@login_required(login_url='login')
def profile_view(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.warning(request,f'Account was not updated!')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
        context={
            'u_form':u_form,
            'p_form':p_form
        }
        return render(request,'profile.html',context)

'''@login_required(login_url='login')
def profile_view(request):
    if request.method=='POST':
        pass
    else:
        context={
            'user':request.user
        }
        return render(request,'profile.html',context)

'''