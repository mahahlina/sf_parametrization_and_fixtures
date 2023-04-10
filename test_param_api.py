import pytest
from api import get_bookings, create_booking


@pytest.mark.smoke
def test_bookings_list():
    response = get_bookings()
    assert response.status_code == 200


@pytest.mark.parametrize("first_name, last_name", [["Test", "Marina"], ["Test1", "Ovchinnikova"]])
def test_create_booking(first_name, last_name):
    response = create_booking(first_name, last_name, 123, True, "2018-01-01", "2018-01-03", "Dog")
    assert response.status_code == 200
