# TaskCraft

TaskCraft is a learning project for building a web application that manages
tasks. The current version uses Flask, server-rendered HTML, and SQLite. It
implements UC-01: creating a private task assigned to its creator.

## Get started

Install the dependencies from the project root:

```powershell
uv sync
```

Start the development server:

```powershell
uv run flask --app app run --debug
```

Open <http://127.0.0.1:5000> in a browser. The Flask application object is
named `app` and is defined in `src/app/__init__.py`. The application creates
its local SQLite database in Flask's `instance` directory when first used.

For a production-like local run on Windows, use Waitress:

```powershell
uv run waitress-serve --listen=127.0.0.1:8000 app:app
```

On Linux or macOS, use Gunicorn:

```bash
uv run gunicorn --bind 127.0.0.1:8000 app:app
```

Then open <http://127.0.0.1:8000>.

## Run the tests

```powershell
uv run pytest
```

## Project structure

 * `src/app/__init__.py` creates the Flask application, defines its routes, and
   handles SQLite persistence.
 * `src/app/templates/` and `src/app/static/` contain the server-rendered
   frontend and its stylesheet.
 * `tests/` contains automated user acceptance tests.
 * `docs/decisions/` records architectural decisions and their tradeoffs.

The initial framework decision is documented in
`docs/decisions/0001-framework-choice.md`.

The initial product behavior is described in `docs/use-cases.md`, and its
conceptual entities and rules are recorded in `docs/data-model.md`.

## Container

Build and run the included Docker image:

```bash
docker build . -t taskcraft
docker run --rm -p 8000:8000 taskcraft
```

Open <http://127.0.0.1:8000>.
