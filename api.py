import requests


def get_bookings():
    return requests.get("https://restful-booker.herokuapp.com/booking")


def create_booking(firstname: str, lastname: str, totalprice: int, depositpaid: bool, checkin, checkout,
                   additionalneeds: str):
    request_body = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }

    return requests.post("https://restful-booker.herokuapp.com/booking", json=request_body)
