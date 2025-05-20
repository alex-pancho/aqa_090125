from pages.base_page import BasePage

class RegistrationPage(BasePage):
    locators = {
        "sign_up_button": '//button[text()="Sign up"]',  # Додано локатор кнопки відкриття модального вікна
        "name_field": '//input[@id="signupName"]',
        "last_name_field": '//input[@id="signupLastName"]',
        "email_field": '//input[@id="signupEmail"]',
        "password_field": '//input[@id="signupPassword"]',
        "repeat_password_field": '//input[@id="signupRepeatPassword"]',
        "register_button": '//button[text()="Register"]'
    }

    def open_registration_modal(self):
        """Відкриває модальне вікно реєстрації."""
        self.click(self.locators["sign_up_button"])

    def fill_form(self, name, last_name, email, password):
        """Заповнює форму реєстрації."""
        self.send_keys(self.locators["name_field"], name)
        self.send_keys(self.locators["last_name_field"], last_name)
        self.send_keys(self.locators["email_field"], email)
        self.send_keys(self.locators["password_field"], password)
        self.send_keys(self.locators["repeat_password_field"], password)

    def submit_form(self):
        """Сабміт форми реєстрації."""
        self.click(self.locators["register_button"])
