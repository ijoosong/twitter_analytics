from app import app


@app.route('/')
@app.route('/index/')
def index():
    return "Hi zach. you're dumb. oh well. :D"
