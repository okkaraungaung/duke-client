from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='assets/client')

@app.get('/')
def serve_client():
    return send_from_directory('assets/client', 'index.html')

app = Flask(__name__)


@app.get('/tasks')
def list_or_find():
    return ''


@app.post('/tasks')
def create():
    return ''


@app.patch('/tasks/<int:id>/mark')
def mark(id: int):
    return ''


@app.patch('/tasks/<int:id>/unmark')
def unmark(id: int):
    return ''


@app.delete('/tasks/<int:id>')
def delete(id: int):
    return ''
