from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    """Serve the application's static landing page."""
    return app.send_static_file("index.html")
