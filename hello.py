from os import name
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'henrique'

class NameForm(FlaskForm):
    name = StringField('Qual e o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Parece que você mudou de nome! ')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def page_serve_error(e):
    return render_template('500.html', current_time=datetime.utcnow()), 500

if __name__=='__main__':
    app.run()