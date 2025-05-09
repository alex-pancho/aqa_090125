from selenium.webdriver.common.by import By
from .hw_elements import WebElement 


class GaragePage(WebElement):
    titele = (By.XPATH, '//h1[.="Garage"]')
    add_car_button = (By.XPATH, '//button[text()="Add car"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
