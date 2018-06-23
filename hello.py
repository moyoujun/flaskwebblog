from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return "<h1>hello world</h1>"


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.route('/agent')
def agent():
    user_agent = request.headers.get('user-Agent')
    return '<p>Your browser is %s</p>' % user_agent


if __name__ == "__main__":
    manager.run()

