import pytest
from pages.home_page import HomePage
from pages.registration_modal import RegistrationModal

class TestRegistration:
    def test_populate_registration_form(self, driver, home_page, registration_page, garage_page):

        home_page.item("sign_up_button").click()
        register = RegistrationModal(driver).item("registration_modal_register_button")
        registration_page.populate_registration_form(
            name="Clara",
            last_name="OswinOswald",
            email="claraoswinoswald@gmail.com",
            password="Test123!"
        )
        assert register.is_clickable()
        registration_page.sign_up()
        assert garage_page.item("add_car").is_visible()
