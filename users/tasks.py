from celery import shared_task

from django.core.mail import send_mail

from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!',
              'Hi, This is proof the task worked!',
              'denuxs@gmail.com',
              ['xijacap681@netjook.com'])

    return None
