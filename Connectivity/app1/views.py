from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.template import RequestContext
from django.core.exceptions import BadRequest
# from portal.models import savePortal
from .models import savePortal
from . import *
# Create your views here.


def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    # def sum(a, b, *args, **kwargs):
    #     ans = a + b
    #     print("hello", ans, args, kwargs)
    #     pass
    # sum(2, 2, 4, 5, 66, 443, 45, 63453, 5435435, 4534, operation="minus")
    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if (pass1 != pass2):
            raise BadRequest("The password doesn't match")
        my_user = User.objects.create_user(
            uname, email, pass1, first_name=name)
        my_user.save()
        # return HttpResponse("User has been created")
        return redirect('login')

    return render(request, 'register.html')


def LoginPage(request):
    return render(request, 'login.html')


def savePortal(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        leaveType = request.POST.get('leaveType')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        reason = request.POST.get('reason')
        newInput = savePortal(name=name, email=email, leaveType=leaveType,
                              startDate=startDate, endDate=endDate, reason=reason)
        newInput.save()
        print("Done scene")
    return render(request, 'home.html')
