import pika
from mail import send_mail

connection = pika.BlockingConnection(pika.ConnectionParameters(
		host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='mails')
print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
	print " [x] Received %r" % (body,)
	send_mail(body)

channel.basic_consume(callback, queue='mails', no_ack=True)

channel.start_consuming()