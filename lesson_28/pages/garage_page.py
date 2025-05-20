from pages.base_page import BasePage

class GaragePage(BasePage):
    locators = {
        "garage_heading": '//h1[contains(text(), "Garage")]'
    }

    def get_heading_text(self):
        """Отримує текст заголовка Garage."""
        return self.item(self.locators["garage_heading"]).text
