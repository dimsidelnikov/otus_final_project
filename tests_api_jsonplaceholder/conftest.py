import pytest
from urllib.parse import urljoin


@pytest.fixture
def base_url():
    base_path = 'https://jsonplaceholder.typicode.com'
    resource_path = 'posts/'
    base_url = urljoin(base_path, resource_path)

    return base_url
