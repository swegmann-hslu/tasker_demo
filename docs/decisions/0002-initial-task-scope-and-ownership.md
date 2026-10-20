# Start with private tasks assigned to their creators

Date: 2026-10-20

## Status

Accepted

## Context

TaskCraft's first functional scope consists of creating, deleting, completing,
and listing tasks. The long-term idea includes team-based task management, but
implementing teams now would also require membership, visibility, assignment,
and permission rules. The initial task data needs a clear ownership model and
a small set of understandable fields.

## Options Considered

 * Private tasks assigned to their creators: keeps authorization and the first
   use cases small, while retaining explicit creator and assignee concepts.
 * Team-visible tasks from the start: supports the longer-term goal sooner, but
   requires team membership and permission behavior before the basic task
   workflows can be learned and implemented.
 * Tasks without ownership: is the smallest data model, but cannot enforce the
   stated requirement that tasks are private.

## Decision

For the first version, every task is private to its creator and is
automatically assigned to that creator. A task stores a required title,
required due date, optional description, creator, assignee, and done state.
Priority is excluded for now.

Deletion is permanent and requires user confirmation. The overview includes
both open and completed tasks without requiring filtering, sorting, searching,
or pagination.

## Reasons

This scope supports all four initial use cases without introducing team and
permission concepts prematurely. Keeping creator and assignee as explicit
references makes the current rule clear and exposes the concepts that will
need reconsideration when team tasks are introduced.

## Consequences

The first implementation must enforce ownership on the backend whenever a task
is read or changed; hiding another user's task only in the frontend is not
sufficient. The application will need a way to identify the current user,
although the authentication approach remains undecided. Reassignment, shared
visibility, archiving, priorities, and overview controls are deferred to later
decisions.
