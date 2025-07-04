import pytest
from API_test.test_data import bodys, headers

def test_preparing_of_server(users_api):
    tes1 = users_api.verify_health_check()
    if tes1 != 0: pytest.fail()

def test_user_register(users_api):
    response = users_api.call_user_register_api(body=bodys.body_for_user_register, headers=headers.header_default)
    test1 = users_api.verify_status_code_is(expected_status_code=201, actual_status_code=response.status_code)
    test2 = users_api.verify_name_is_correct(response_body=response.json(), expected_name=users_api.name)
    test3 = users_api.verify_email_is_correct(response_body=response.json(), expected_email=users_api.email)
    if test1 + test2 + test3 != 0: pytest.fail()

def test_user_register_with_exists_email(users_api):
    response = users_api.call_user_register_api(body=bodys.body_for_user_register, headers=headers.header_default)
    test1 = users_api.verify_status_code_is(expected_status_code=409, actual_status_code=response.status_code)
    test2 = users_api.verify_status_massage_for_exists_user(response_body=response.json())
    if test1 + test2 != 0: pytest.fail()

def test_user_login(users_api):
    response = users_api.call_user_login_api(body=bodys.body_for_user_login, headers=headers.header_default)
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = users_api.verify_name_is_correct(response_body=response.json(), expected_name=users_api.name)
    test3 = users_api.verify_email_is_correct(response_body=response.json(), expected_email=users_api.email)
    if test1 + test2 + test3 != 0: pytest.fail()

def test_user_login_with_incorrect_email_and_password(users_api):
    response = users_api.call_user_login_api(body=bodys.body_for_user_login_with_incorrect_data, headers=headers.header_default)
    test1 = users_api.verify_status_code_is(expected_status_code=401, actual_status_code=response.status_code)
    test2 = users_api.verify_status_massage_for_login_incorrect_data(response_body=response.json())
    if test1 + test2 != 0: pytest.fail()

def test_user_profile_get(users_api, get_token):
    response = users_api.call_user_profile_api(headers=users_api.get_default_header_with_auth(get_token))
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = users_api.verify_name_is_correct(response_body=response.json(), expected_name=users_api.name)
    test3 = users_api.verify_email_is_correct(response_body=response.json(), expected_email=users_api.email)
    if test1 + test2 + test3 != 0: pytest.fail()

def test_user_edit_profile(users_api, get_token):
    response = users_api.call_edit_profile_api(body=bodys.body_for_edit_profile, headers=users_api.get_default_header_with_auth(get_token))
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = users_api.verify_phone_number_is_correct(response_body=response.json(), expected_phone_number=users_api.phone)
    test3 = users_api.verify_company_name_is_correct(response_body=response.json(), expected_company_name=users_api.company)
    if test1 + test2 + test3 != 0: pytest.fail()

def test_user_logout(users_api, get_token):
    response = users_api.call_user_logout_api(headers=users_api.get_default_header_with_auth(get_token))
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: pytest.fail()

def test_user_delete(users_api, get_token):
    response = users_api.call_user_delete_api(headers=users_api.get_default_header_with_auth(get_token))
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: pytest.fail()