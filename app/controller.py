from flask import render_template
from app import app
from app.models.events_list import events

@app.route('/')
def index():
    # normal python function
    return render_template('index.html', title='Home', events=events)

@app.route('/events')
def events_list():
    # normal python function
    return render_template('events.html', title='Events', events=events)