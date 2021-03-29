from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'


class EmailForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    subject = StringField('Subject')
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')


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


def sendemail():
    pass


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
