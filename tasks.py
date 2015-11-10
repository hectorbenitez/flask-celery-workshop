from celery.task import task
from mail import send_mail


@task
def send_mail_async(email):
	send_mail(email)