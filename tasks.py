from mail import send_mail
from celery import Celery

celery_app = Celery('app', broker='amqp://nmungaja:oivkBuMaChhuLut4kfuHadHyBtrU9nhi@tiger.cloudamqp.com/nmungaja')

@celery_app.task
def send_mail_async(email):
	send_mail(email)