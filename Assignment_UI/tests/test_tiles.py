import time
from Assignment_UI.locators.locators import SEARCH_ICON_FIELD,SEARCH_BAR_INPUT_FIELD,HEADER_SEARCH_RESULT_FIELD
# from locators.locators import *
def test_tiles_pass(browser, base_url):
    """
    Test to verify that the page title is correct.
    """
    browser.get(base_url)
    Search = browser.find_element("xpath",SEARCH_ICON_FIELD)

    time.sleep(4)
    Search.click()
    time.sleep(2)
    Search_bar = browser.find_element("xpath", SEARCH_BAR_INPUT_FIELD).send_keys("IFRS 17")
    time.sleep(2)
    header_search_results = browser.find_elements("xpath", HEADER_SEARCH_RESULT_FIELD)
    # time.sleep(2)
    print(header_search_results)
    print(len(header_search_results))
    for i in header_search_results:
        print(i)
    assert len(header_search_results) == 5

def test_tiles_fail(browser, base_url):
    """
    Test to verify that the page tiles is correct.
    """
    browser.get(base_url)

    Search = browser.find_element("xpath", SEARCH_ICON_FIELD)

    time.sleep(4)
    Search.click()
    time.sleep(2)
    Search_bar = browser.find_element("xpath", SEARCH_BAR_INPUT_FIELD)
    time.sleep(2)
    header_search_results = browser.find_elements("xpath", HEADER_SEARCH_RESULT_FIELD)

    print(header_search_results)
    print(len(header_search_results))
    for i in header_search_results:
        print(i)
    assert len(header_search_results) == 4