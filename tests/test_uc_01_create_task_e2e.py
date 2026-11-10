from playwright.sync_api import Page, expect


def test_user_adds_a_new_task_in_the_browser(page: Page, live_server):
    page.goto(live_server)

    page.get_by_label("Title").fill("Prepare browser demo")
    page.get_by_label("Description").fill("Show the complete TaskCraft workflow")
    page.get_by_label("Due date").fill("2026-11-20")
    page.get_by_role("button", name="Create task").click()

    expect(page.get_by_role("status")).to_have_text("Task created successfully.")

    created_task = page.get_by_role("listitem").filter(has_text="Prepare browser demo")
    expect(created_task).to_contain_text("Show the complete TaskCraft workflow")
    expect(created_task).to_contain_text("2026-11-20")
    expect(created_task).to_contain_text("Open")
