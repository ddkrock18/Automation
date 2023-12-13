import pytest
import requests




def test_req_mo_get():
    response = requests.get("https://restful-booker.herokuapp.com/booking/")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_post_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers,json= payload)
    print(response.text)
    print(response.json()["token"])
    assert response.status_code == 200

def test_post_create_booking():
    payload_create_booking={
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
            "additionalneeds": "Breakfast"
    }
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers, json=payload_create_booking)
    print(response.json())
    print(response.headers)
    bookingid = response.json()["bookingid"]
    assert response.status_code == 200