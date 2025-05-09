import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage


class TestRegistration:
    def test_fill_registration_form(self, home_page, registration_page):
        
        home_page.item("sign_up_button").click()
        
        
        registration_page.fill_registration_form(
            name="Kseniya",
            last_name="Karnaukh",
            email="test0123@gmail.com",
            password="Qwerty41"
        )
        
        
        registration_page.submit_registration()
        
        
        import time
        time.sleep(3)