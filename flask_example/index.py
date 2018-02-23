from flask import render_template, request, Flask

"""Example for a simple Flask application. Uses bulma.io as css framework."""

app = Flask(__name__)


@app.route('/')
def index():
    """If the request is a http-get, the parameters name and age will be displayed."""
    return render_template('index.html',
                           title='Dominik Strässle',
                           items=request.args.items(),
                           name=request.args.get('name', default=None),
                           age=request.args.get('age', default=None))


if __name__ == '__main__':
    """Runs only in debug mode if the app isn't excecuted remotely."""
    app.run(debug=True)
