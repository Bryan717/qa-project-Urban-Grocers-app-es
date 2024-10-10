# data.py

default_kit_body = {
    "name": "default kit name"
}

def get_kit_body(name):
    body = default_kit_body.copy()
    body["name"] = name
    return body


headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}