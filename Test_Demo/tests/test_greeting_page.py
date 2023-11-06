import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tests.pages.greeting_actions import GreetingActions
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("url", ["file:///D:/QAOPS_DEMO/Website_demo/index.html",])
@pytest.mark.parametrize("name", ["John", "", "Jack",])
def test_greeting_page(browser, url, name):
    greeting_actions = GreetingActions(browser)

    greeting_actions.get_to_page(url)
    time.sleep(2)

    greeting_actions.submit_name(name)
    time.sleep(2)

    actual_greeting = greeting_actions.get_greeting()
    expected_greeting = f"Hello, {name}!"

    if name != "":
        assert actual_greeting == expected_greeting
    else:
        assert actual_greeting == "" and expected_greeting != "Hello, !"

