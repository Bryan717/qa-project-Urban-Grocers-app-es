# sender_stand_request.py

import requests
from configuration import BASE_URL, CREATE_USER_ROUTE, CREATE_KIT_ROUTE


def get_new_user_token():
    # Simula la creación de un nuevo usuario y devuelve el token de autenticación
    response = requests.post(f"{BASE_URL}{CREATE_USER_ROUTE}")

    # Imprimir el status code de la respuesta
    print(f"Status Code: {response.status_code}")

    # Imprimir el token de autenticación
    auth_token = response.json().get("authToken", "")
    print(f"Auth Token: {auth_token}")

    return auth_token


def post_new_client_kit(kit_body, auth_token="jknnFApafP4awfAIFfafam2fma"):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(f"{BASE_URL}{CREATE_KIT_ROUTE}", json=kit_body, headers=headers)

    # Imprimir el status code de la respuesta al crear el kit
    print(f"Kit Creation Status Code: {response.status_code}")

    return response

