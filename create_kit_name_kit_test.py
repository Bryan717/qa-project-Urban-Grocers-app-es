# create_kit_name_kit_test.py

import pytest
from sender_stand_request import get_new_user_token, post_new_client_kit
from data import get_kit_body

# Funciones de ayuda
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# Pruebas
def test_minimum_allowed_characters():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_maximum_allowed_characters():
    kit_body = get_kit_body("Abcd..." * 63)  # 511 caracteres
    positive_assert(kit_body)

def test_zero_characters():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_more_than_maximum_characters():
    kit_body = get_kit_body("Abcd..." * 64)  # 512 caracteres
    negative_assert_code_400(kit_body)

def test_special_characters_allowed():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

def test_spaces_allowed():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

def test_numbers_allowed():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_no_name_field():
    kit_body = {}
    negative_assert_code_400(kit_body)

def test_name_as_number():
    kit_body = get_kit_body(123)  # No debe ser número
    negative_assert_code_400(kit_body)
