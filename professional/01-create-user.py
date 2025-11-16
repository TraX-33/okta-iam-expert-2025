#!/usr/bin/env python3
"""
Okta User Creation – Équivalent CA IM Provisioning
@author: TraX-33 | Décembre 2025
"""

import requests

# === CONFIG À REMPLIR APRÈS CRÉATION TENANT ===
OKTA_DOMAIN = "https://dev-XXXXXX.okta.com"      # ← ton domaine
API_TOKEN = "ssws_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # ← Admin → Security → API → Create Token

headers = {
    "Authorization": f"SSWS {API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def create_user(email, first_name, last_name):
    payload = {
        "profile": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "login": email
        },
        "credentials": {
            "password": {"value": "TempPass2025!"}
        }
    }
    
    response = requests.post(
        f"{OKTA_DOMAIN}/api/v1/users?activate=true",
        json=payload,
        headers=headers
    )
    
    if response.status_code == 200:
        user_id = response.json()["id"]
        print(f"Utilisateur créé ! ID : {user_id}")
    else:
        print(f"Erreur {response.status_code} : {response.text}")

if __name__ == "__main__":
    create_user("test.user@demo.com", "Test", "User")
