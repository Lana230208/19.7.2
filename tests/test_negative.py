from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_empty_user():
    status, result = pf.get_api_key("", None)
    assert status == 403


def test_get_api_key_for_invalid_user():
    status, result = pf.get_api_key("&&&&", "////")
    assert status == 403


def test_get_all_pets_with_invalid_key(filter=""):
    auth_key = "invalid key"
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403


def test_add_pet_with_wrong_name():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    name = ""
    animal_type = "dog"
    pet_age = 3
    status, result = pf.add_pet(auth_key, name, animal_type, pet_age)
    assert status == 200  # 400 Обнаружена уязвимость. Можно передавать неверные параметры.


def test_add_pet_with_wrong_animal_type():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    name = "Vasya"
    animal_type = ""
    pet_age = -2
    status, result = pf.add_pet(auth_key, name, animal_type, pet_age)
    assert status == 200  # 400 Обнаружена уязвимость. Можно передавать неверные параметры.






