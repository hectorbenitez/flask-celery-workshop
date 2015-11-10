from celery import Celery
from flask import Flask, request, render_template, session, redirect, url_for
from tasks import send_mail_async

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'amqp://localhost:5672'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    email = request.form['email']
    send_mail_async.delay(email)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
