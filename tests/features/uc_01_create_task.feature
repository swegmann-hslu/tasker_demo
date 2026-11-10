Feature: Create a task
  As a user
  I want to record a task I need to complete
  So that it appears in my task overview

  Scenario: Create a task with valid information
    Given the user has opened TaskCraft
    When the user creates a task titled "Prepare BDD demo" with description "Review the readable scenario with students" due on "2026-11-20"
    Then the application confirms that the task was created
    And the task overview shows "Prepare BDD demo" as "Open"
