from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboardapp.forms import SignupForm

@login_required
def check(request):
    return render(request,'temp/home.html')

def Signup_view(request):
    form=SignupForm()
    if request.method =='POST':
        form = SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'temp/signup.html',{'form':form})


def logout_view(request):
    return render(request,'temp/logout.html')

def about_view(request):
    return render(request,'temp/about.html')