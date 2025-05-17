from pages.base_page import BasePage


class RegistrationModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        registration_modal = '//app-signup-modal',
        registration_modal_name_input = '//app-signup-modal//input[@id="signupName"]',
        registration_modal_last_name_input = '//app-signup-modal//input[@id="signupLastName"]',
        registration_modal_email_input = '//app-signup-modal//input[@id="signupEmail"]',
        registration_modal_password_input = '//app-signup-modal//input[@id="signupPassword"]',
        registration_modal_reenter_password_input = '//app-signup-modal//input[@id="signupRepeatPassword"]',
        registration_modal_register_button = '//app-signup-modal//button[text()="Register"]',
        registration_modal_register_button_disabled = '//app-signup-modal//button[@disabled and text()="Register"]',
        registration_modal_register_button_enabled = '//app-signup-modal//button[not(@disabled) and text()="Register"]'
        )

    def populate_registration_form(self, name, last_name, email, password):
        self.item("registration_modal_name_input").send_keys(name)
        self.item("registration_modal_last_name_input").send_keys(last_name)
        self.item("registration_modal_email_input").send_keys(email)
        self.item("registration_modal_password_input").send_keys(password)
        self.item("registration_modal_reenter_password_input").send_keys(password)

    def sign_up(self):
        self.item("registration_modal_register_button_enabled").click()
