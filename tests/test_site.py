import requests


def test_url_status(base_url, exp_code):
    response = requests.get(base_url)
    assert response.status_code == int(exp_code)
