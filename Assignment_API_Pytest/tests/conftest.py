import requests
import pytest
import os
import time


@pytest.fixture(scope="function")
def post_request():
    """Test the POST method of an API."""
    # Base URL and endpoint
    base_url = "https://api.restful-api.dev"
    endpoint = "/objects"

    # Full URL
    url = f"{base_url}{endpoint}"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_api_key_here"
    }

    # Payload (Body of the POST request)
    payload = {
            "name": "Test Assignment API",
            "data": {
                "year": 2020,
                "price": 24000,
                "CPU model": "Intel Core i9",
                "Hard disk size": "2 TB"
            }
    }

    try:
        # Send POST request
        response = requests.post(url, json=payload, headers=headers)

        # Print the status code and response JSON
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
        print("Response JSON ID :", response.json().get("id"))
        ID_for_PATCH_METHOD = response.json().get("id")
        # global ID_for_PATCH_METHOD
        # # Assertions
        # assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        # assert response.json().get("id") is not None, "User ID not returned in response"
        #
        # print("POST request test passed!")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except AssertionError as e:
        print(f"Test failed: {e}")

    yield ID_for_PATCH_METHOD

# Capture screenshot and attach to the report on test failure
def pytest_runtest_makereport(item, call):
    # Only capture screenshot if the test failed
    if call.excinfo is not None:
        # Get the browser instance from the test fixture
        browser = item.funcargs.get('browser')

        if browser:
            # Create the screenshots directory if it doesn't exist
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            # Capture screenshot with a timestamp
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = os.path.join(screenshot_dir, f"{item.nodeid}_{timestamp}.png")
            browser.save_screenshot(screenshot_path)

            # Attach the screenshot to the HTML report
            if not os.path.exists('reports'):
                os.makedirs('reports')

            if "pytest_html" in item.config.pluginmanager.get_plugins():
                extra = getattr(item, "extra", [])
                extra.append(pytest.html.extras.image(screenshot_path))
                item.extra = extra


# Attach screenshots and extra information to the HTML report
def pytest_html_report_title(report):
    report.title = "Test Report with Screenshots"

@pytest.fixture(scope="session")
def base_url(config):
    """
    Get the base_url value from the loaded configuration.
    """
    return config["base_url"]

