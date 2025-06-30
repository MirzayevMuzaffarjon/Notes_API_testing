import pytest
from API_test.test_data import bodys, headers


def test_preparing_of_server(users_api):
    tes1 = users_api.verify_health_check()
    if tes1 == 0:
        response = users_api.call_user_register_api(body=bodys.body_for_user_register, headers=headers.header_default)
        test2 = users_api.verify_status_code_is(expected_status_code=201, actual_status_code=response.status_code)
        if test2 != 0: pytest.fail()
    else: pytest.fail()

def test_create_home_note(notes_api, get_token):
    response = notes_api.call_create_notes_api(body=bodys.body_for_create_home_notes, headers=notes_api.get_default_header_with_auth(get_token))
    global home_note_id
    home_note_id = response.json()["data"]["id"]
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = notes_api.verify_status_massage(response_body=response.json())
    if test1 + test2 != 0: pytest.fail()

def test_get_home_note(notes_api, get_token):
    response = notes_api.call_get_notes_api(note_id=home_note_id, headers=notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = notes_api.verify_note_title(expected_title=notes_api.home_note_title, response_body=response.json())
    test3 = notes_api.verify_note_description(expected_description=notes_api.home_note_description, response_body=response.json())
    test4 = notes_api.verify_note_category(expected_category=notes_api.home_note_category, response_body=response.json())
    if test1 + test2 + test3 + test4 != 0: pytest.fail()

def test_create_work_note(notes_api, get_token):
    response = notes_api.call_create_notes_api(body=bodys.body_for_create_work_notes, headers=notes_api.get_default_header_with_auth(get_token))
    global work_note_id
    work_note_id = response.json()["data"]["id"]
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = notes_api.verify_status_massage(response_body=response.json())
    if test1 + test2 != 0: pytest.fail()

def test_get_work_note(notes_api, get_token):
    response = notes_api.call_get_notes_api(note_id=work_note_id, headers=notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = notes_api.verify_note_title(expected_title=notes_api.work_note_title, response_body=response.json())
    test3 = notes_api.verify_note_description(expected_description=notes_api.work_note_description, response_body=response.json())
    test4 = notes_api.verify_note_category(expected_category=notes_api.work_note_category, response_body=response.json())
    if test1 + test2 + test3 + test4 != 0: pytest.fail()

def test_create_personal_note(notes_api, get_token):
    response = notes_api.call_create_notes_api(body=bodys.body_for_create_personal_notes, headers=notes_api.get_default_header_with_auth(get_token))
    global personal_note_id
    personal_note_id = response.json()["data"]["id"]
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = notes_api.verify_status_massage(response_body=response.json())
    if test1 + test2 != 0: pytest.fail()

def test_get_personal_note(notes_api, get_token):
    response = notes_api.call_get_notes_api(note_id=personal_note_id, headers=notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    test2 = notes_api.verify_note_title(expected_title=notes_api.personal_note_title, response_body=response.json())
    test3 = notes_api.verify_note_description(expected_description=notes_api.personal_note_description, response_body=response.json())
    test4 = notes_api.verify_note_category(expected_category=notes_api.personal_note_category, response_body=response.json())
    if test1 + test2 + test3 + test4 != 0: pytest.fail()

def test_get_list_of_notes(notes_api, get_token):
    response = notes_api.call_get_notes_list_api(notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: pytest.fail()

def test_delete_home_note(notes_api, get_token):
    response = notes_api.call_delete_notes_api(note_id=home_note_id, headers=notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: pytest.fail()

def test_delete_work_note(notes_api, get_token):
    response = notes_api.call_delete_notes_api(note_id=work_note_id, headers=notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: pytest.fail()

def test_delete_personal_note(notes_api, get_token):
    response = notes_api.call_delete_notes_api(note_id=personal_note_id, headers=notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: pytest.fail()

def test_user_delete(users_api, get_token):
    response = users_api.call_user_delete_api(headers=users_api.get_default_header_with_auth(get_token))
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: pytest.fail()