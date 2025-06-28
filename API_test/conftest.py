import pytest, logging
from API_test.test_data import bodys, headers
from APIs.Users import UsersAPI
from  APIs.Notes import NotesAPI


@pytest.fixture(scope="function")
def users_api():
    return UsersAPI()

@pytest.fixture(scope="function")
def notes_api():
    return NotesAPI()

@pytest.fixture(scope="function")
def get_token(users_api):
    max_iteration = 10
    token = ""
    login_response = users_api.call_user_login_api(body=bodys.body_for_user_login, headers=headers.header_default)
    if login_response.status_code == 200:
        token = login_response.json()["data"]["token"]
    elif login_response.status_code == 401:
        register_response = users_api.call_user_register_api(body=bodys.body_for_user_register, headers=headers.header_default)
        if register_response.status_code == 201:
            login_response = users_api.call_user_login_api(body=bodys.body_for_user_login, headers=headers.header_default)
            token = login_response.json()["data"]["token"]
        else: logging.warning(f"\n---Error while register user!!!")
    else: logging.warning(f"\n---Error while getting token!!!")
    while token == "" and max_iteration != 0:
        get_token(users_api)
        max_iteration = max_iteration - 1
    return token


