from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings


def send_massage(request):
    send_massage = Info.objects.first()

    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            email,
            [ settings.EMAIL_HOST_USER],
        )

    return render(request, 'contact/contact.html', {'send_massage': send_massage})