import requests
import pytest


#@pytest.mark.http
#def test_first_http():
#    r = requests.get('https://api.github.com/zen')
#    print(f"Answer is {r.text}")


@pytest.mark.http
def second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f"Response Body is {r.json()}")
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers is {r.headers}")