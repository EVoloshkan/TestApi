import pytest
import requests


def send_request(path, status_code=200, status="success"):
    response = requests.get(path)
    assert response.status_code == status_code
    assert response.headers['content-type'] == 'application/json'
    data = response.json()
    assert data['status'] == status
    return data


def test_list_all_breeds():
    data = send_request('https://dog.ceo/api/breeds/list/all')


def test_random_image():
    data = send_request('https://dog.ceo/api/breeds/image/random')
    assert data['message'] != ''


@pytest.mark.parametrize("cond", [
    'corgi/cardigan',
    'husky'
])
def test_breeds_list(cond):
    data = send_request('https://dog.ceo/api/breed/' + cond + '/images/random')


def test_breeds_list_all():
    data = send_request('https://dog.ceo/api/breeds/list/all')
    for item in data['message']:
        data = send_request('https://dog.ceo/api/breed/' + item + '/images/random')


@pytest.mark.parametrize("cond", [
    'asdasd',
    'asdad'
])
def test_breeds_list_negative(cond):
    data = send_request('https://dog.ceo/api/breed/' + cond + '/images/random', 404, 'error')
