# Persist initial tasks in SQLite with a configurable placeholder identity

ID: ADR-01K9R3F8W8N6Q5T7V2C4M1X0ZA

Date: 2026-11-10

## Status

Accepted

## Context

UC-01 requires created tasks to be stored, assigned to the current user, and
shown in that user's overview. Authentication and production database choices
are deliberately outside the current scope. The implementation should remain
small and understandable while still exercising a complete browser-to-database
workflow.

## Options Considered

 * Store tasks in memory: requires almost no setup, but loses tasks whenever the
   process restarts and does not demonstrate persistence.
 * Store tasks in SQLite and configure a placeholder current-user identifier:
   provides durable local storage with Python's standard library, while making
   the temporary identity boundary explicit.
 * Add a database library and authentication now: more closely resembles a
   production system, but introduces concepts not required by UC-01.

## Decision

Use SQLite through Python's standard library for the first task workflow. Read
the current-user identifier from Flask configuration, with `demo-user` as the
local default and an override for automated tests.

## Reasons

SQLite provides real persistence without a separate service or new dependency.
A configured identity allows the backend to enforce creator and assignee rules
without pretending that authentication has already been designed. Both choices
keep the full workflow visible to students.

## Consequences

The application stores tasks between restarts and acceptance tests can use an
isolated database. The configured user is not authentication and must not be
treated as secure. A later authentication decision must replace it, and a more
capable database or migration tool may be needed as the domain grows.
