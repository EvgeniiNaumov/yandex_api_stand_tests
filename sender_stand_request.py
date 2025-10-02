import requests
from configuration import URL_SERVICE, PATH_CREATE_USER, PATH_CREATE_KIT

def post_new_user(user_body):
    return requests.post(URL_SERVICE + PATH_CREATE_USER, json=user_body)

def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(URL_SERVICE + PATH_CREATE_KIT, json=kit_body, headers=headers)