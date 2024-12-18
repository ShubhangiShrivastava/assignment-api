import pytest
from selenium import webdriver
import yaml
import os
import time

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture(scope="session")
def config():
    """
    Load the configuration file and return its content as a dictionary.
    """
    with open("data/config.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="function")
def browser(request,config):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.maximize_window()
    implicit_wait = config.get("timeout", 10)  # Default to 10 seconds if not set
    driver.implicitly_wait(implicit_wait)
    yield driver
    driver.quit()

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