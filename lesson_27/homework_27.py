from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TrackingNovaPoshta:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_tracking_page(self, url="https://tracking.novaposhta.ua/#/uk"):
        """Відкриває сторінку трекінгу."""
        self.driver.get(url)

    def enter_tracking_number(self, track_number):
        """Вводить номер накладної у відповідне поле."""
        try:
            input_field = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "track__form-group-input"))
            )
            input_field.clear()
            input_field.send_keys(track_number)
        except TimeoutException:
            raise TimeoutException("Поле введення номера не було знайдено на сторінці.")

    def click_search_button(self):
        """Натискає кнопку пошуку."""
        try:
            search_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "track__form-group-btn"))
            )
            search_button.click()
        except TimeoutException:
            raise TimeoutException("Кнопку 'Пошук' не вдалося знайти або натиснути.")

    def get_tracking_status(self):
        """Отримує статус посилки."""
        try:
            result_status = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "header__status-text"))
            )
            return result_status.text.strip()
        except TimeoutException:
            raise TimeoutException("Статус посилки не вдалося отримати.")
