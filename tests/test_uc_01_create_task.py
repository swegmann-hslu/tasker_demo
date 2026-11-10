def test_user_can_create_task_and_see_it_in_overview(client, stored_tasks):
    response = client.post(
        "/tasks",
        data={
            "title": "Prepare project demo",
            "description": "Rehearse the main workflow",
            "due_date": "2026-11-20",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Task created successfully." in response.data
    assert b"Prepare project demo" in response.data
    assert b"Rehearse the main workflow" in response.data
    assert b"2026-11-20" in response.data
    assert b"user-123" in response.data
    assert b"Open" in response.data

    tasks = stored_tasks()
    assert len(tasks) == 1
    task = tasks[0]
    assert task["id"]
    assert task["title"] == "Prepare project demo"
    assert task["description"] == "Rehearse the main workflow"
    assert task["due_date"] == "2026-11-20"
    assert task["creator_id"] == "user-123"
    assert task["assignee_id"] == "user-123"
    assert task["is_done"] == 0


def test_description_may_be_empty(client, stored_tasks):
    response = client.post(
        "/tasks",
        data={"title": "Submit report", "description": "", "due_date": "2026-12-01"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert stored_tasks()[0]["description"] == ""


def test_missing_required_fields_are_explained_and_task_is_not_created(
    client, stored_tasks
):
    response = client.post(
        "/tasks",
        data={"title": "   ", "description": "Optional details", "due_date": ""},
    )

    assert response.status_code == 400
    assert b"Title is required." in response.data
    assert b"Due date is required." in response.data
    assert stored_tasks() == []


def test_invalid_due_date_is_explained_and_task_is_not_created(client, stored_tasks):
    response = client.post(
        "/tasks",
        data={
            "title": "Impossible deadline",
            "description": "",
            "due_date": "2026-02-30",
        },
    )

    assert response.status_code == 400
    assert b"Enter a valid due date." in response.data
    assert b"Impossible deadline" in response.data
    assert stored_tasks() == []


def test_create_form_and_empty_overview_are_shown(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Create a task" in response.data
    assert b'name="title"' in response.data
    assert b'name="description"' in response.data
    assert b'name="due_date"' in response.data
    assert b"No tasks yet. Create your first task above." in response.data
