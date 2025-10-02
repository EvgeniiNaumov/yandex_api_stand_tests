import sender_stand_request
import data


# Получение токена пользователя
def get_user_token():
    res = sender_stand_request.post_new_user(data.user_body)
    json_data = res.json()
    return json_data['authToken']


# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_char_in_name_get_success():
    kit_body = {"name": "a"}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_chars_in_name_get_success():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    }
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_0_chars_in_name_get_error():
    kit_body = {"name": ""}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_chars_in_name_get_error():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    }
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# Тест 5. Разрешены английские буквы
def test_create_kit_english_letters_in_name_get_success():
    kit_body = {"name": "QWErty"}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Тест 6. Разрешены русские буквы
def test_create_kit_russian_letters_in_name_get_success():
    kit_body = {"name": "Набор"}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Тест 7. Разрешены спецсимволы
def test_create_kit_special_symbols_in_name_get_success():
    kit_body = {"name": "\"№%@\","}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Тест 8. Разрешены пробелы
def test_create_kit_spaces_in_name_get_success():
    kit_body = {"name": " Набор второй "}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Тест 9. Разрешены цифры
def test_create_kit_numbers_in_name_get_success():
    kit_body = {"name": "123"}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Тест 10. Параметр не передан в запросе
def test_create_kit_no_name_param_get_error():
    kit_body = {}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# Тест 11. Передан другой тип параметра (число)
def test_create_kit_number_type_in_name_get_error():
    kit_body = {"name": 123}
    token = get_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400
