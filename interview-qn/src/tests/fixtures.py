import pytest

@pytest.fixture
def add_user_log():
  return {
    "activity_type": "Add user",
    "target_id": "1",
    "old_value": None,
    "new_value": {
      "display_name": "John",
      "username": "john321"
    },
    "change_timestamp": 1650333433,
  }

@pytest.fixture
def update_app_log():
  return {
    "activity_type": "Updated app",
    "target_id": "2",
    "old_value": {
      "display_name": "Calendar App",
      "permissions": ["Calendar.Read"]
    },
    "new_value": {
      "display_name": "Calendar App",
      "permissions": ["Calendar.Read", "Mail.ReadWrite"]
    },
    "change_timestamp": 1650333433,
  }