from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.exceptions import BadRequest
# Create your views here.


def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
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
