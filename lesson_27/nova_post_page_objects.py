from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NovaPoshtaTrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_tracking_page(self, url):
        """Відкриває сторінку відстеження."""
        self.driver.get(url)

    def enter_tracking_number(self, tracking_number):
        """Вводить номер накладної у відповідне поле."""
        tracking_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='track__form-group-input']"))
        )
        tracking_input.send_keys(tracking_number)

    def click_track_button(self):
        """Натискає кнопку 'Відстежити'."""
        track_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='track__form-group-btn green-active']"))
        )
        track_button.click()

    def get_parcel_status(self):
        """Отримує статус посилки з елементу на сторінці."""
        status_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='header__status-text']"))
        )
        return status_element.text.strip()