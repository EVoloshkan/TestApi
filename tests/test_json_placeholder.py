import pytest
import requests


@pytest.mark.parametrize("cond", [
    1,
    3,
    7
])
def test_json_placeholder(cond):
    response = requests.get('https://jsonplaceholder.typicode.com/todos/' + str(cond))
    assert response.status_code == 200
    body = response.json()
    assert body != ''
    assert body['id'] == cond


def test_placeholder_post():
    data = {'userId': 1, 'title': 'foo', 'body': 'bar'}
    response = requests.post('https://jsonplaceholder.typicode.com/todos', data)
    assert response.status_code == 201
    body = response.json()
    assert body['id'] > 0


@pytest.mark.parametrize("cond", [
    ({'userId': 1, 'title': 'foo', 'body': 'bar', 'id': 1}),
    ({'userId': 5, 'title': 'foo', 'body': 'bar', 'id': 17}),
    ({'userId': 3, 'title': 'foo', 'body': 'bar', 'id': 4})
])
def test_placeholder_put(cond):
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1', cond)
    assert response.status_code == 200
    body = response.json()
    assert body['id'] > 0
    assert body['title'] == cond['title']


def test_placeholder_photos():
    response = requests.get('https://jsonplaceholder.typicode.com/albums/1/photos')
    assert response.status_code == 200
    body = response.json()
    assert len(body) > 0
    for album in body:
        assert album['albumId'] == 1


@pytest.mark.parametrize("cond", [
    1,
    4,
    7
])
def test_placeholder_delete(cond):
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/' + str(cond))
