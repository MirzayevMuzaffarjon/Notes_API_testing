from API_test.test_data import bodys, headers


def test_preparing_of_server(users_api):
    tes1 = users_api.verify_health_check()
    if tes1 == 0:
        response = users_api.call_user_register_api(body=bodys.body_for_user_register, headers=headers.header_default)
        test2 = users_api.verify_status_code_is(expected_status_code=201, actual_status_code=response.status_code)
        if test2 != 0: raise
    else: raise


def test_create_home_note(notes_api, get_token):
    response = notes_api.call_create_notes_api(
        body=bodys.body_for_create_home_notes,
        headers=notes_api.get_default_header_with_auth(get_token) )
    global home_note_id
    home_note_id = response.json()["data"]["id"]
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: raise

def test_delete_home_note(notes_api, get_token):
    response = notes_api.call_delete_notes_api(note_id=home_note_id, headers=notes_api.get_default_header_with_auth(get_token))
    test1 = notes_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: raise

def test_user_delete(users_api, get_token):
    response = users_api.call_user_delete_api(headers=users_api.get_default_header_with_auth(get_token))
    test1 = users_api.verify_status_code_is(expected_status_code=200, actual_status_code=response.status_code)
    if test1 != 0: raise
