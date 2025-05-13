from selenium.webdriver.common.by import By

from lesson_27.processing_element import ProcessingPage


class TrackingNovaposhtaPage(ProcessingPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    package_number_input = (By.XPATH, '//input[@class="track__form-group-input"]')
    search_button = (By.XPATH, '//input[@class="track__form-group-btn green-active"]')
    package_number_text = (By.XPATH, '//div[@class="header__status"]')
    package_status_text = (By.XPATH, '//div[@class="header__status-text"]')
