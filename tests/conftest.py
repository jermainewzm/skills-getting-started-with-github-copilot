from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    original_activities = deepcopy(activities)
    client = TestClient(app)
    yield client
    activities.clear()
    activities.update(original_activities)
