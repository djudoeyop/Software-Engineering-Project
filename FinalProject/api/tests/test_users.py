from fastapi.testclient import TestClient
from ..controllers import users as controller
from ..main import app
import pytest
from ..models import users as model
from ..schemas.users import UserCreate

# Create a test client using the FastAPI app
client = TestClient(app)

@pytest.fixture
def mock_db_session(mocker):
    # This fixture mocks the database session
    return mocker.Mock()

def test_create_user(mock_db_session):
    # Prepare user data
    user_data = {
        "username": "johndoe",
        "employmentStatus": "employed"
    }
    user_object = UserCreate(**user_data)

    # Assuming the controller has a method to create a user
    created_user = controller.create_user(mock_db_session, user_object)

    # Assertions to ensure the user is created correctly
    assert created_user is not None
    assert created_user.username == "johndoe"
    assert created_user.employmentStatus == "employed"
