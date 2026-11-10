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

Install the Chromium browser used by the end-to-end test once:

```powershell
uv run playwright install chromium
```

Then run the complete test suite in headless mode:

```powershell
uv run pytest
```

On a Linux CI agent, install Chromium and its operating-system dependencies
before running pytest:

```bash
uv run playwright install --with-deps chromium
uv run pytest
```

To watch the browser workflow locally while debugging it, run:

```powershell
uv run pytest tests/test_uc_01_create_task_e2e.py --headed
```

## Project structure

 * `src/app/__init__.py` creates the Flask application, defines its routes, and
   handles SQLite persistence.
 * `src/app/templates/` and `src/app/static/` contain the server-rendered
   frontend and its stylesheet.
 * `tests/` contains Flask integration tests and a Playwright browser acceptance
   test.
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
