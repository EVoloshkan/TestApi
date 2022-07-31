import pytest
import requests


def send_request(path, status_code=200):
    response = requests.get(path)
    assert response.status_code == status_code
    assert response.headers['content-type'] == 'application/json; charset=utf-8'
    return response.json()


@pytest.mark.parametrize("cond", [
    'madtree-brewing-cincinnati',
    'circle-9-brewing-san-diego'
])
def test_single_brewery(cond):
    body = send_request('https://api.openbrewerydb.org/breweries/' + cond)
    assert body['id'] == cond


@pytest.mark.parametrize("cond", [
    15,
    4,
    0
])
def test_breweries_per_page(cond):
    body = send_request('https://api.openbrewerydb.org/breweries?per_page=' + str(cond))
    assert len(body) == cond


@pytest.mark.parametrize("cond, exp", [
    (('new_york', 20), "New York"),
    (('california', 20), "California"),
    (('florida', 20), "Florida")
])
def test_breweries_by_state_per_page(cond, exp):
    body = send_request('https://api.openbrewerydb.org/breweries?by_state=' + cond[0] + '& per_page=' + str(cond[1]))
    assert len(body) == cond[1]
    for state in body:
        assert state['state'] == exp


@pytest.mark.parametrize("cond", [
    ('nano'),
    ('brewpub'),
    ('bar'),
    ('closed')
])
def test_by_type(cond):
    body = send_request('https://api.openbrewerydb.org/breweries?by_type=' + cond + '&per_page=3')
    for type in body:
        assert type['brewery_type'] == cond


def test_random_brewery():
    body = send_request('https://api.openbrewerydb.org/breweries/random')
    assert body != ''
