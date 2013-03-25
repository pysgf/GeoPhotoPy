from GeoPhotoPy import app
import flask

@app.route('/')
def index():
    return flask.render_template('index.html')
