from flask import render_template
from app import app


@app.route('/')
@app.route('/index/')
def index():
    user = {'name': 'Zach'}
    tweets = [
        {
            'username': 'ijoosong',
            'message': 'Lol is this thing working?'
        },
        {
            'username': 'inpursuitofswag',
            'message': 'lawlz you aint know crap'
        }
    ]
    return render_template('index.html', title='Home', user=user, tweets=tweets)
