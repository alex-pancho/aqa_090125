from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        name_input='//input[@id="signupName"]',
        last_name_input='//input[@id="signupLastName"]',
        email_input='//input[@id="signupEmail"]',
        password_input='//input[@id="signupPassword"]',
        repeat_password_input='//input[@id="signupRepeatPassword"]',
        register_button='//button[.="Register"]',
        error_message='//div[contains(@class, "invalid-feedback")]',
        success_register='//h1[contains(text(), "Garage")]'
    )

    def fill_registration_form(self, name, last_name, email, password):
        self.item("name_input").send_keys(name)
        self.item("last_name_input").send_keys(last_name)
        self.item("email_input").send_keys(email)
        self.item("password_input").send_keys(password)
        self.item("repeat_password_input").send_keys(password)
    
    def submit_registration(self):
        self.item("register_button").click()