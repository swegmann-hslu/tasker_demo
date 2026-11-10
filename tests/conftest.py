import sqlite3
from threading import Thread

import pytest
from werkzeug.serving import make_server

from app import create_app


@pytest.fixture
def database_path(tmp_path):
    return tmp_path / "taskcraft-test.sqlite"


@pytest.fixture
def app(database_path):
    return create_app(
        {
            "TESTING": True,
            "DATABASE": str(database_path),
            "CURRENT_USER_ID": "user-123",
        }
    )


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def live_server(app):
    """Run the test application on a free local port for browser tests."""
    server = make_server("127.0.0.1", 0, app, threaded=True)
    server_thread = Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server_thread.join()


@pytest.fixture
def stored_tasks(database_path):
    def load_tasks():
        connection = sqlite3.connect(database_path)
        connection.row_factory = sqlite3.Row
        try:
            return connection.execute("SELECT * FROM tasks ORDER BY title").fetchall()
        finally:
            connection.close()

    return load_tasks
