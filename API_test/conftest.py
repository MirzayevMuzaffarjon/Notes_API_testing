import pytest
from API_test.test_data import parameters, bodys, headers
from APIs.Users import UsersAPI

@pytest.fixture(scope="function")
def users_api():
    return UsersAPI()

@pytest.fixture(scope="function")
def get_token(users_api):
    response = users_api.call_user_login_api(body=bodys.body_for_user_login, headers=headers.header_default)
    token = response.json()["data"]["token"]
    return token