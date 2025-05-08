from selenium.webdriver.common.by import By

from lesson_28.pages.processing_page import ProcessingPage


class HillelGaragePage(ProcessingPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    add_car_button = (By.XPATH, '//button[text()="Add car"]')
