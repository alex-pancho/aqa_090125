from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class NovaPoshtaTracker:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_tracking_page(self, url="https://tracking.novaposhta.ua/#/uk"):
        self.driver.get(url)

    def enter_tracking_number(self, tracking_number: str):
        input_field = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#en"))
        )
        input_field.clear()
        if not tracking_number.isdigit() or len(tracking_number) < 11:
            raise ValueError("Номер накладної повинен містити щонайменше 11 цифр")
        input_field.send_keys(tracking_number)

    def submit_tracking_request(self):
        try:
            search_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "np-number-input-desktop-btn-search-en"))
            )
            search_button.click()
        except TimeoutException:
            raise TimeoutException("Кнопка 'Пошук' не стала активною у заданий час")

    def read_status(self) -> str:
        try:
            status_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'header__status-header')]/following-sibling::div[contains(@class, 'header__status-text')]"))
            )
            return status_element.text.strip()
        except TimeoutException:
            return "Статус не знайдено"

    def get_parcel_status(self, tracking_number: str, url: str = "https://tracking.novaposhta.ua/#/uk") -> str:
        self.open_tracking_page(url)
        self.enter_tracking_number(tracking_number)
        self.submit_tracking_request()
        return self.read_status()