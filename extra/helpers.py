import json


def load_auth_token():
    with open('extra/auth.json') as f:
        data = json.load(f)
        return data['Authorization']


def load_fhir_server():
    with open('extra/auth.json') as f:
        data = json.load(f)
        return data['FhirServer']
