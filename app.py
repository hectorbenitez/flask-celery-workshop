from flask import Flask, request, render_template, session, redirect, url_for
from mail import send_mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    email = request.form['email']
    send_mail(email)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
