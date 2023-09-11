from flask import Flask


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
