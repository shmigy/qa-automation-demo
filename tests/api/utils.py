import requests

def get_json(url, headers=None):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def post_json(url, payload, headers=None):
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()
