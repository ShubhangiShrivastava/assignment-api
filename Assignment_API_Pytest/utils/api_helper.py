import requests
import json

def base_url(config):
    """
    Get the base_url value from the loaded configuration.
    """
    BASE_URL = config["base_url"]
    return BASE_URL

def patch_method(id, payload):
    """Sends a PATCH request and returns the response."""
    url = f"{base_url}/{id}"
    headers = {

    }
    try:
        response = requests.patch(url, headers=headers, json=payload)
        print(f"PATCH {url} with payload {json.dumps(payload)}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}\n")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
