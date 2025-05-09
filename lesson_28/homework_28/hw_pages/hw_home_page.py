from selenium.webdriver.common.by import By
from .hw_elements import WebElement 


class HomePageHillel(WebElement):
    sign_up_button = (By.XPATH, '//button[text()="Sign up"]')
    registration_popup = (By.XPATH, '//h4[.="Registration"]')
    sign_up_name_input = (By.XPATH, '//input[@id="signupName"]')
    sign_up_last_name_input = (By.XPATH, '//input[@id="signupLastName"]')
    sign_up_email_input = (By.XPATH, '//input[@id="signupEmail"]')
    sign_up_password_input = (By.XPATH, '//input[@id="signupPassword"]')
    sign_up_repeat_password_input = (By.XPATH, '//input[@id="signupRepeatPassword"]')
    register_button = (By.XPATH, '//button[text()="Register"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
