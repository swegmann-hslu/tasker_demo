import sqlite3

import pytest

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
def stored_tasks(database_path):
    def load_tasks():
        connection = sqlite3.connect(database_path)
        connection.row_factory = sqlite3.Row
        try:
            return connection.execute("SELECT * FROM tasks ORDER BY title").fetchall()
        finally:
            connection.close()

    return load_tasks
