# Use pytest-bdd for readable executable acceptance specifications

ID: ADR-01K9R7A4C6D8E2F5G0H3J1MNPQ

Date: 2026-11-10

## Status

Accepted

## Context

TaskCraft already tests UC-01 with Flask integration tests and a direct
Playwright browser test. Students should also be able to explore an ATDD/BDD
style in which stakeholders can review behavior in a human-readable Gherkin
feature file while the scenario remains automatically executable.

## Options Considered

 * Keep only Python test functions: requires no additional framework, but the
   workflow remains mixed with browser automation details.
 * Use Behave: offers a mature Gherkin workflow, but introduces a separate test
   runner, fixture system, and CI command alongside pytest.
 * Use pytest-bdd: adds Gherkin feature files while reusing pytest, the existing
   Playwright page fixture, and the isolated TaskCraft live server.

## Decision

Add pytest-bdd and express the successful UC-01 browser journey as an
executable Gherkin scenario. Keep the existing Flask and direct Playwright
tests in parallel so students can compare the approaches.

## Reasons

pytest-bdd provides the requested separation between readable examples and
automation code without splitting the test suite across runners. Reusing the
existing fixtures keeps the example focused on BDD concepts rather than test
infrastructure.

## Consequences

The same happy-path workflow is intentionally represented twice for teaching
and comparison. Gherkin scenarios need matching Python step definitions, which
adds indirection and maintenance. Future scenarios should use business
language and cover behavior valuable to reviewers rather than merely restating
low-level interface actions.
