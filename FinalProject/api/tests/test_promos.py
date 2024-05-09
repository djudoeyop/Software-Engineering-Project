from fastapi.testclient import TestClient
from ..controllers import users as controller
from ..main import app
import pytest
from ..models import promos as model
from ..controllers import promos as controller
from ..schemas.promos import PromoCreate



client = TestClient(app)

@pytest.fixture
def mock_db_session(mocker):
    # This fixture mocks the database session
    return mocker.Mock()

def test_create_promo(mock_db_session):
    # Prepare promo data
    promo_data = {
        "promoText": "Promo code",
        "amount": 10,
        "user_id": 1  # Provide a user_id here
    }
    promo_object = PromoCreate(**promo_data)

    # Mocking the return value of the controller method
    mock_created_promo = model.Promo(**promo_data)
    mock_db_session.add.return_value = mock_created_promo

    # Assuming the controller has a method to create a promo
    created_promo = controller.create_promo(mock_db_session, promo_object)

    # Assertions to ensure the promo is created correctly
    assert created_promo is not None
    assert created_promo.promoText == "Promo code"
    assert created_promo.amount == 10


