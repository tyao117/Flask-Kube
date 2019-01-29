from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tim'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }, 
        {
            'author': {'username': 'Blazer'},
            'body': 'Lolz, this blog is too basic'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)