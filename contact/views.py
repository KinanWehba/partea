from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
)


    

    return render(request, 'contact/contact.html')
def send_message(request):

    

    return render(request, 'contact/contact1.html')