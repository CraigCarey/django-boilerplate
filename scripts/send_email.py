#! /usr/bin/env python3

from django.conf import settings
from django.core.mail import send_mail

subject = 'this is the subject'
from_email = settings.DEFAULT_FROM_EMAIL
message = 'This is my test message'
recipient_list = ['lknkjsdhfkjhsd09879bnasdfbs@gmail.com']
html_message = 'this is the body'
send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
