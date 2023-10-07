from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='assets/client')

@app.get('/')
def serve_client():
    return send_from_directory('assets/client', 'index.html')