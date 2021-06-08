from django.shortcuts import render, redirect
from django.http import HttpResponse
from email_send.settings import BASE_DIR
from email_sending_cli import send_email

def home(request):
    if request.method == 'GET':
        return render(request, 'mail/home.html')
    else:
        email_from = request.POST.get('email_from')
        email_to = request.POST.get('email_to')
        mail = request.POST.get('email_text')
        print(email_to.split(','))
        send_email(email_from, email_to.split(','), mail)
        return redirect('home-view')
