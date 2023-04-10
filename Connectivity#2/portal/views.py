from django.shortcuts import render

# Create your views here.


def savePortal(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        email = request.POST.get('email')
        leaveType = request.POST.get('leaveType')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        reason = request.POST.get('reason')
        en = savePortal(pname=pname, email=email, leaveType=leaveType,
                        startDate=startDate, endDate=endDate, reason=reason)
        en.save()
    return render(request, 'home.html')
