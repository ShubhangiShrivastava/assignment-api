import requests
from Assignment_API_Pytest.utils.api_helper import patch_method
import json

# TestCase_1: Valid request with all fields updated
def test_patch_valid_update(post_request):
    test = {post_request}
    print(test)
    test = test.pop()
    ENDPOINT= test.replace("'","")
    print(ENDPOINT)
    body = {"name": "Test_patch_valid_update", "data": {"year":"2024"}}
    patch_method(ENDPOINT, body)

# TestCase_2: Valid request with partial fields
def test_patch_partial_update(post_request):
    test = {post_request}
    print(test)
    test = test.pop()
    ENDPOINT = test.replace("'", "")
    print(ENDPOINT)
    body = {"name": "test_patch_partial_update"}  # Only updating status
    patch_method(ENDPOINT, body)

# TestCase_3: ID is not existing resource
def test_patch_non_existent_resource():
    body = {"name": "test_patch_non_existent_resource", "data": {"year":"2024"}}
    patch_method("9999", body)  # Assuming 9999 does not exist

# TestCase_4: Invalid data types of name in body
def test_patch_invalid_data(post_request):
    test = {post_request}
    print(test)
    test = test.pop()
    ENDPOINT = test.replace("'", "")
    print(ENDPOINT)
    body = {"name": 12345, "data": {"year":"2024"}}  # Invalid data types/values
    patch_method(ENDPOINT, body)

# TestCase_5: No data in body
def test_patch_empty_body(post_request):
    test = {post_request}
    print(test)
    test = test.pop()
    ENDPOINT = test.replace("'", "")
    print(ENDPOINT)
    body = {}
    patch_method(ENDPOINT, body)

# TestCase_6: Special characters and edge cases as part of body
def test_patch_special_characters(post_request):
    test = {post_request}
    print(test)
    test = test.pop()
    ENDPOINT = test.replace("'", "")
    print(ENDPOINT)
    body = {"name": "<script>alert('xss')</script>", "data": {"year":"2024"}}
    patch_method(ENDPOINT, body)

# TestCase_7: Large data in body
def test_patch_large_body(post_request):
    test = {post_request}
    print(test)
    test = test.pop()
    ENDPOINT = test.replace("'", "")
    print(ENDPOINT)
    large_text = "a" * 10000  # String with 10,000 characters
    body = {"name": large_text, "data": {"year":"2025"}}
    patch_method(ENDPOINT, body)

# TestCase_8: Unauthorized request
def test_patch_unauthorized(post_request):
    test = {post_request}
    print(test)
    test = test.pop()
    ENDPOINT = test.replace("'", "")
    print(ENDPOINT)
    url = "https://api.restful-api.dev"
    url = f"{url}/{ENDPOINT}"
    body = {"name": "Unauthorized Name"}
    response = requests.patch(url, headers={"Content-Type": "application/json"}, json=body)  # No auth header
    print(f"PATCH {url} with body {json.dumps(body)}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}\n")