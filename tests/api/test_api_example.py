import pytest
from utils import get_json

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_posts():
    data = get_json(f"{BASE_URL}/posts")
    assert isinstance(data, list)
    assert len(data) > 0
    assert "userId" in data[0]
