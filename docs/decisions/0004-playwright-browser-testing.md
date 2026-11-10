# Use Playwright for a small set of browser acceptance tests

ID: ADR-01K9R5P2E7F4G8H3J6M0N1Q9ST

Date: 2026-11-10

## Status

Accepted

## Context

The Flask test client verifies UC-01 from the HTTP request through persistence
and rendered HTML, but it does not operate the application through a browser.
TaskCraft needs confidence that critical user workflows also work in a real
browser and can be tested without a graphical desktop on a CI server.

## Options Considered

 * Keep only Flask test-client tests: fast and simple, but does not verify
   browser interaction.
 * Add a small Playwright test suite using headless Chromium: verifies critical
   workflows in a browser and integrates with pytest, at the cost of installing
   a browser binary.
 * Duplicate the full acceptance suite across several browsers: offers broader
   compatibility coverage, but adds runtime and maintenance beyond the current
   learning scope.

## Decision

Use the Playwright pytest plugin with headless Chromium for selected critical
workflows. Begin with the successful UC-01 task-creation journey. Keep detailed
validation and persistence assertions in the faster Flask integration tests.

## Reasons

This adds genuine browser coverage without introducing a frontend build system
or a separate test runner. One focused journey demonstrates the boundary
between browser and server tests while keeping local and CI execution small.

## Consequences

Developers and CI agents must install the Playwright Chromium binary before
running the complete suite. Browser tests are slower than Flask test-client
tests, so they should remain focused on high-value user journeys. Developers
can run the same tests with a visible browser when diagnosing failures.
