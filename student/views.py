from django.shortcuts import render,redirect,HttpResponsePermanentRedirect
from . models import *
from .form import StudentApplicationForm
from django.views import View
from .forms import RegisterForm
from datetime import timedelta
from django.utils import timezone

# =======================STUDENTREGISTER=======================
def delete_expired_notifications():
    expired_notifications = Notification.objects.filter(time__lte=timezone.now() - timedelta(minutes=2880))
    expired_notifications.delete()


def student_register(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            new_student = form.save()

            # Create a notification for the new student
            current_time = timezone.now()
            notification = Notification.objects.create(student=new_student, time=current_time)
            notification.save()

            Notification.delete_expired_notifications()  # Manually call the function to delete expired notifications
            return HttpResponsePermanentRedirect('/')
        else:
            return render(request, 'application.html', {'form': form})
    else:
        form = StudentApplicationForm()
        return render(request, 'application.html', {'form': form})
# =======================ENDSTUDENT=======================


def id_student(request,id_st):
    notifications=Notification.objects.all()
    student_id = StudentApplication.objects.get(id=id_st)
    return render(request, 'idcard/ID_card.html',{'student_id':student_id,'notifications':notifications})

def student_request(request):
    notifications=Notification.objects.all()
    st_request = StudentApplication.objects.filter(accepted=False)
    return render(request, 'request/student_request.html',{'st_request':st_request,'notifications':notifications})

def student_accept(request, st_id):
    if request.method == 'POST':
        student = StudentApplication.objects.get(id=st_id)
        student.accepted = True
        student.save()
        return redirect('student_request')
    
def student_waiting_profile(request,swp_id):
    notifications=Notification.objects.all()
    sw_profile = StudentApplication.objects.filter(id=swp_id)
    return render(request, 'request/student_waiting_profile.html',{'sw_profile':sw_profile,'notifications':notifications})
