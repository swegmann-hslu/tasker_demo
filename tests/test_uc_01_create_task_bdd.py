from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenario, then, when


@scenario(
    "features/uc_01_create_task.feature",
    "Create a task with valid information",
)
def test_create_a_task_with_valid_information():
    """Execute the human-readable UC-01 scenario."""


@given("the user has opened TaskCraft")
def open_taskcraft(page: Page, live_server):
    page.goto(live_server)


@when(
    parsers.parse(
        'the user creates a task titled "{title}" with description "{description}" '
        'due on "{due_date}"'
    )
)
def create_task(page: Page, title: str, description: str, due_date: str):
    page.get_by_label("Title").fill(title)
    page.get_by_label("Description").fill(description)
    page.get_by_label("Due date").fill(due_date)
    page.get_by_role("button", name="Create task").click()


@then("the application confirms that the task was created")
def task_creation_is_confirmed(page: Page):
    expect(page.get_by_role("status")).to_have_text("Task created successfully.")


@then(parsers.parse('the task overview shows "{title}" as "{status}"'))
def task_appears_in_overview(page: Page, title: str, status: str):
    created_task = page.get_by_role("listitem").filter(has_text=title)
    expect(created_task).to_contain_text(status)
