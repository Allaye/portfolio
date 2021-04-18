import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
load_dotenv(find_dotenv())
app.config['SECRET_KEY'] = 'a really really really really long secret key'
address = os.environ.get('email')
password = os.environ.get('password')


class EmailForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    subject = StringField('Subject')
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')


def sendemail(name, subject, email, message):
    msg = EmailMessage()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(os.environ.get('mail_server'), os.environ.get('mail_port'), context=context) as server:
        server.login(address, password) 
        msg['Subject'] = subject
        msg['From'] = address
        msg['To'] = address
        msg.set_content(f"send_name: {name} sender_email: {email} \n{message}")
        server.send_message(msg)


@app.route('/', methods=['POST', 'GET'])
def index():
    form = EmailForm()
    if form.validate_on_submit():
        name = request.form['name']
        subject = form.subject.data
        email = request.form['email']
        message = form.message.data
        sendemail(name, subject, email, message)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


@app.route('/project')
def project():
    return render_template('project.html')


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
