import allure
import pytest
import requests
from jsonschema import validate
from urllib.parse import urljoin


@pytest.mark.parametrize('id_post, id_user', [(1, 1), (12, 2), (25, 3)], ids=['post 1 user 1',
                                                                              'post 12 user 2',
                                                                              'post 25 user 3'])
def test_positive_update_resource(request, base_url, id_post, id_user):
    allure.dynamic.title(f'Позитивный тест обновления ресурса [{request.node.callspec.id}]')
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json = {
        'id': id_post,
        'title': 'foo',
        'body': 'bar',
        'userId': id_user
    }

    response = requests.put(url=urljoin(base_url, str(id_post)), headers=headers, json=json)
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'userId': {'type': 'number'},
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'body': {'type': 'string'}
        },
        'required': ['userId', 'id', 'title', 'body']
    }

    validate(instance=response.json(), schema=schema)
    assert response.json().get('title') == json['title']
    assert response.json().get('body') == json['body']
    assert response.json().get('userId') == id_user
    assert response.json().get('id') == id_post


@pytest.mark.parametrize('id_post, id_user, expected_status_code', [(0, 1, 404),
                                                                    (101, 10, 404),
                                                                    ('id', 3, 400),
                                                                    ('', 1, 400)],
                         ids=['post 0 user 1',
                              'post 101 user 10',
                              'post string user 3',
                              'post empty user 1'])
def test_negative_update_resource(request, base_url, id_post, id_user, expected_status_code):
    allure.dynamic.title(f'Негативный тест обновления ресурса [{request.node.callspec.id}]')
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json = {
        'id': id_post,
        'title': 'foo',
        'body': 'bar',
        'userId': id_user
    }

    response = requests.put(url=urljoin(base_url, str(id_post)), headers=headers, json=json)
    assert response.status_code == expected_status_code
