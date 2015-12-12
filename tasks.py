from celery import chord
from celery.task import task
from mail import send_mail


@task
def send_mail_async(email):
	send_mail(email)


@task
def done_async(result):
	print result
	print 'Done!!!'


def send_mail_with_chord(email):
	chord([send_mail_async.s(email), send_mail_async.s('admin@mail.com')])(done_async.s())