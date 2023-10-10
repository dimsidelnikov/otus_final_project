import allure
import requests
from jsonschema import validate


@allure.title("Тест создания ресурса")
def test_create_resource(base_url):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    response = requests.post(url=base_url, headers=headers, json=json)
    assert response.status_code == 201

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
    assert response.json().get('userId') == json['userId']
