import requests
import pytest


#@pytest.mark.http
#def test_first_http():
#    r = requests.get('https://api.github.com/zen')
#    print(f"Answer is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    #print(f"Response Body is {r.json()}")
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_user_address_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404