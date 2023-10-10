import allure
import pytest
import requests
from urllib.parse import urljoin


@pytest.mark.parametrize('id_post', [1, 12, 100], ids=['post 1 user 1',
                                                       'post 12 user 2',
                                                       'post 100 user 10'])
def test_positive_delete_resource(request, base_url, id_post):
    allure.dynamic.title(f'Позитивный тест удаления ресурса [{request.node.callspec.id}]')
    response = requests.delete(urljoin(base_url, str(id_post)))
    assert response.status_code == 200


@pytest.mark.parametrize('id_post, expected_status_code', [(0, 404), (101, 404), ('id', 400), ('', 400)],
                         ids=['0',
                              'exceeds the maximum',
                              'string',
                              'empty'])
def test_negative_delete_resource(request, base_url, id_post, expected_status_code):
    allure.dynamic.title(f'Негативный тест удаления ресурса с id [{request.node.callspec.id}]')
    response = requests.delete(urljoin(base_url, str(id_post)))
    assert response.status_code == expected_status_code
