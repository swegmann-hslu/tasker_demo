import sqlite3
from datetime import date
from pathlib import Path
from uuid import uuid4

from flask import Flask, current_app, g, redirect, render_template, request, url_for


def create_app(test_config=None):
    """Create and configure the TaskCraft Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=str(Path(app.instance_path) / "taskcraft.sqlite"),
        CURRENT_USER_ID="demo-user",
    )

    if test_config:
        app.config.update(test_config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    app.teardown_appcontext(close_database)

    @app.before_request
    def prepare_database():
        initialize_database()

    @app.get("/")
    def index():
        return render_task_overview(created=request.args.get("created") == "1")

    @app.post("/tasks")
    def create_task():
        form_data = {
            "title": request.form.get("title", "").strip(),
            "description": request.form.get("description", "").strip(),
            "due_date": request.form.get("due_date", "").strip(),
        }
        errors = validate_task(form_data)

        if errors:
            return render_task_overview(form_data=form_data, errors=errors), 400

        user_id = current_app.config["CURRENT_USER_ID"]
        database = get_database()
        database.execute(
            """
            INSERT INTO tasks (
                id, title, description, due_date, creator_id, assignee_id, is_done
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(uuid4()),
                form_data["title"],
                form_data["description"],
                form_data["due_date"],
                user_id,
                user_id,
                False,
            ),
        )
        database.commit()

        return redirect(url_for("index", created=1))

    return app


def validate_task(form_data):
    """Return field-specific validation errors for submitted task data."""
    errors = {}

    if not form_data["title"]:
        errors["title"] = "Title is required."

    if not form_data["due_date"]:
        errors["due_date"] = "Due date is required."
    else:
        try:
            date.fromisoformat(form_data["due_date"])
        except ValueError:
            errors["due_date"] = "Enter a valid due date."

    return errors


def render_task_overview(form_data=None, errors=None, created=False):
    """Render the create form and the current user's task overview."""
    user_id = current_app.config["CURRENT_USER_ID"]
    tasks = (
        get_database()
        .execute(
            """
        SELECT id, title, description, due_date, assignee_id, is_done
        FROM tasks
        WHERE creator_id = ?
        ORDER BY due_date, title
        """,
            (user_id,),
        )
        .fetchall()
    )
    return render_template(
        "index.html",
        tasks=tasks,
        form_data=form_data or {},
        errors=errors or {},
        created=created,
    )


def get_database():
    """Open one SQLite connection for the current request."""
    if "database" not in g:
        g.database = sqlite3.connect(current_app.config["DATABASE"])
        g.database.row_factory = sqlite3.Row
    return g.database


def close_database(_error=None):
    """Close the request's SQLite connection, if one was opened."""
    database = g.pop("database", None)
    if database is not None:
        database.close()


def initialize_database():
    """Create the task table the first time the application is used."""
    database = get_database()
    database.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL CHECK (length(trim(title)) > 0),
            description TEXT NOT NULL DEFAULT '',
            due_date TEXT NOT NULL,
            creator_id TEXT NOT NULL,
            assignee_id TEXT NOT NULL CHECK (assignee_id = creator_id),
            is_done INTEGER NOT NULL DEFAULT 0 CHECK (is_done IN (0, 1))
        )
        """
    )
    database.commit()


app = create_app()
