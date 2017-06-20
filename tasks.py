from mail import send_mail
from celery import Celery

config = {}
config['CELERY_BROKER_URL'] = 'amqp://nmungaja:oivkBuMaChhuLut4kfuHadHyBtrU9nhi@tiger.cloudamqp.com/nmungaja'
config['CELERY_RESULT_BACKEND'] = 'redis://localhost:32782/0'

celery_app = Celery('app', broker='amqp://nmungaja:oivkBuMaChhuLut4kfuHadHyBtrU9nhi@tiger.cloudamqp.com/nmungaja')
celery_app.conf.update(config)


@celery_app.task
def send_mail_async(email):
	send_mail(email)