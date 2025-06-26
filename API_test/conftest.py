import pytest
from APIs.Users import UsersAPI

@pytest.fixture(scope="function")
def users_api():
    return UsersAPI()