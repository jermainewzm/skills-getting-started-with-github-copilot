def test_signup_for_activity_adds_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "alex@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Signed up alex@mergington.edu for Chess Club"}


def test_signup_for_nonexistent_activity_returns_404(client):
    response = client.post(
        "/activities/Nonexistent/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_participant_returns_400(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
