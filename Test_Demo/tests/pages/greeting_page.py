from selenium.webdriver.common.by import By


class GreetingPage:
    def __init__(self, driver):
        self.driver = driver

    name_input = (By.ID, "name")
    submit_button = (By.XPATH, "//button[@type='submit']")
    greeting_message = (By.ID, "greeting-message")

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_greeting_message(self):
        return self.driver.find_element(*self.greeting_message)