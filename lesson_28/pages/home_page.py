from pages.base_page import BasePage

class HomePage(BasePage):
    locators = {
        "sign_up_button": '//button[text()="Sign up"]'
    }

    def open_registration_modal(self):
        """Відкриває модальне вікно реєстрації."""
        self.click(self.locators["sign_up_button"])
