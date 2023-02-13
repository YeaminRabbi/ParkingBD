from django.conf import settings
from django.core.mail import send_mail
# from django.contrib.auth import User


def send_email_token(email, token):
    try:
        subject = 'welcome to ParkingBD'
        message = f'Hi, thank you for registering in ParkingBD. Please verify your email by clicking on the link below:http://localhost:8000/varify-email/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except Exception as e:
        print(e)
        return False
    return True