from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some hard to guess string'
# 密码不应该直接写进代码文件，应该写于配置文件。
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template("index.html", current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.route('/agent')
def agent():
    user_agent = request.headers.get('user-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(Form):
    name = StringField('What is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == "__main__":
    manager.run()

