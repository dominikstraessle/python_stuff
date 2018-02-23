from time import sleep

from flask import Flask, Response, stream_with_context
from oracle_dbtools.oracle_dbcm import ConnectionManager, CMError

"""Example for implementing a stream response. Uses bulma.io as css framework."""

app = Flask(__name__)


def get_data() -> list:
    """Query and fetches the required data and returns them as a list."""
    try:
        # Opening database connection with the ConnectionManager
        with ConnectionManager(('user', 'password', 'connection_info')) as cursor:
            # Query data
            cursor.execute("""select id, name from schema.employees""")
            # fetch and return all results
            return cursor.fetchall()
    except CMError as e:
        print(e)


def stream_template(template_name, **context):
    """Thanks to huiliu[1]
    [1]::[https://gist.github.com/huiliu/46be335427605960fa84]"""
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.disable_buffering()
    return rv


def generate():
    """Generator function returning one line of the fetched data per times."""
    # sort the data by id before generating
    for item in sorted(get_data(), key=lambda x: x[0]):
        yield item
        # print them also in the command line
        print(item)
        # sleep to make the effect of streaming visible
        sleep(0.1)


@app.route('/')
def stream_view() -> Response:
    """/"""
    # Generator
    rows = generate()
    # returns Response to stream the data
    return Response(stream_with_context(stream_template('layouts/row.html', rows=rows)))


if __name__ == '__main__':
    """Runs only in debug mode if the app isn't excecuted remotely."""
    app.run(debug=True)
