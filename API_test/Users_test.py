import logging
from API_test.test_data import parameters, bodys, headers


def test_register_user(users_api):
    response = users_api.call_user_register_api(body=bodys.body_for_user_register, headers=headers.header_default)
    test1 = users_api.verify_status_code_is(expected_status_code=201, actual_status_code=response.status_code)
    print(response.json())

    if test1 != 0: raise

def test_user_login(users_api):
    response = users_api.call_user_login_api(body=bodys.body_for_user_login, headers=headers.header_default)
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    print(response.json())
    if test1 != 0: raise

def test_user_delete(users_api, get_token):
    token = get_token
    header = {
        "Content-Type": "application/json",
        "x-auth-token": token
    }
    response = users_api.call_user_delete_api(headers=header)
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: raise