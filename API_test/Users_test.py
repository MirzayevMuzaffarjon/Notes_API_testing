from API_test.test_data import parameters, bodys, headers


def test_register_user(users_api):
    test1 = users_api.verify_health_check()
    response = users_api.call_user_register_api(body=bodys.body_for_user_register, headers=headers.header_for_user_register)
    test2 = users_api.verify_status_code_is(expected_status_code=201, actual_status_code=response.status_code)
    print(response.json())

    if test1 + test2 != 0: raise