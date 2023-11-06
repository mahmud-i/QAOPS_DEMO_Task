from tests.pages.greeting_page import GreetingPage


class GreetingActions:
    def __init__(self, driver):
        self.greeting_page = GreetingPage(driver)

    def get_to_page(self, url):
        self.greeting_page.driver.get(url)

    def submit_name(self, name):
        self.greeting_page.enter_name(name)
        self.greeting_page.click_submit()

    def get_greeting(self):
        return self.greeting_page.get_greeting_message().text

