import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert body['blog'] == 'http://chriswanstrath.com/'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'
    assert headers['Cache-Control'] == 'public, max-age=60, s-maxage=60'


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/sergii_butenko")

    assert r.status_code == 404    



    #print(r.text.encode("utf-8"))
    #print(f"Response Status code is {r.status_code}")
    #print(f"Response Body is {r.json()}".encode("utf-8"))
    #print(f"Response Headers are {r.headers}")