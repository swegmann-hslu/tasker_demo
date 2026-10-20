# Use Flask with a static HTML frontend

Date: 2026-10-17

## Status

Accepted

## Context

TaskCraft needs an initial web application that serves a static HTML page. The
project is intended for learning full-stack development, so the first version
should make the request/response flow easy to understand and should not require
a frontend build tool.

## Options Considered

 * Keep the hand-written WSGI application: minimal dependencies, but routing and
   other web application behavior would need to be implemented manually.
 * Use Flask with static HTML: adds a small framework while keeping the backend
   and frontend structure straightforward.
 * Use Django or a JavaScript single-page application: provides more built-in
   features, but adds concepts and tooling that the current milestone does not
   require.

## Decision

Use Flask for the Python backend and serve a plain HTML file from Flask's
`static` directory. The developer selected Flask and a simple static page for
the first version.

## Reasons

Flask offers routing, testing utilities, and a path for future backend features
without obscuring the basic web concepts. Plain HTML avoids a frontend build
step and keeps the initial application small enough to study in full.

## Consequences

The application is simple to run and extend, and Flask's test client can verify
routes without starting a server. The team will need to introduce its own
application structure as features are added. More comprehensive frameworks or
frontend tooling can be reconsidered if future requirements justify them.
