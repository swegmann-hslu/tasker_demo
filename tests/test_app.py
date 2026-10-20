from app import app


def test_index_serves_static_html():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert b"<h1>TaskCraft</h1>" in response.data
    assert b"Hello from Flask." in response.data
