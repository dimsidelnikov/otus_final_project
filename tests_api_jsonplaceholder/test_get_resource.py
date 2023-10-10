import allure
import pytest
import requests
from jsonschema import validate
from urllib.parse import urljoin


@pytest.mark.parametrize('id_post', [1, 10, 100])
def test_positive_get_resource(request, base_url, id_post):
    allure.dynamic.title(f'Позитивный тест получения инфо о ресурсе с id [{request.node.callspec.id}]')
    response = requests.get(urljoin(base_url, str(id_post)))
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
    assert response.json().get('id') == id_post


@pytest.mark.parametrize('id_post, expected_status_code', [(0, 404), (101, 404), ('id', 400)],
                         ids=['0', 'exceeds the maximum', 'string'])
def test_negative_get_resource(request, base_url, id_post, expected_status_code):
    allure.dynamic.title(f'Негативный тест получения инфо о ресурсе с id [{request.node.callspec.id}]')
    response = requests.get(urljoin(base_url, str(id_post)))
    assert response.status_code == expected_status_code
    assert len(response.json()) == 0


@allure.title("Тест получения инфо обо всех ресурсах")
def test_get_all_resources(base_url):
    response = requests.get(base_url)
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

    for post in response.json():
        validate(instance=post, schema=schema)
