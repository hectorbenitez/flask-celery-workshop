from celery import Celery
from celery.result import AsyncResult
from flask import Flask, request, render_template, session, redirect, url_for
from tasks import send_mail_async

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'amqp://nmungaja:oivkBuMaChhuLut4kfuHadHyBtrU9nhi@tiger.cloudamqp.com/nmungaja'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:32782/0'

# Initialize Celery
celery = Celery(app.name)
celery.conf.update(app.config)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    email = request.form['email']
    async_result = send_mail_async.delay(email)
    print async_result.id

    return redirect(url_for('index'))


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template('result.html')

    result_id = request.form['result_id']
    async_result = celery.AsyncResult(result_id)
    print async_result.status
    print async_result.ready()
    print async_result.failed()
    print async_result.successful()

    return redirect(url_for('result'))

if __name__ == '__main__':
    app.run(debug=True)
