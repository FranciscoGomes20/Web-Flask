from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_serve_error(e):
    return render_template('500.html'), 500

if __name__=='__main__':
    app.run()