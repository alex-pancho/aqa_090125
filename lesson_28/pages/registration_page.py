from pages.base_page import BasePage

class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        sign_up_button = '//button[.="Sign up"]',
        name_field = '//*[@id="signupName"]',
        last_name_field = '//*[@id="signupLastName"]',
        email_field = '//*[@id="signupEmail"]',
        password_field = '//*[@id="signupPassword"]',
        re_enter_password_field = '//*[@id="signupRepeatPassword"]',
        register_button = '//button[contains(@class, "btn-primary") and normalize-space()="Register"]',
        close_icon = '//span[@aria-hidden="true" and text()="×"]',
        garage_heading = '//h1[normalize-space()="Garage"]'

    )

