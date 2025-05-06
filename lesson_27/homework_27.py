from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrackingNovaPoshta:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def tracking_page(self, url):
        self.driver.get(url)

    def enter_track_number(self, track_number):
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "track__form-group-input")))
        element.clear()
        element.send_keys(track_number)

    def click_button(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "track__form-group-btn")))
        button.click()

    def get_status(self):
        status = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header__status-text")))
        return status.text.strip()
    
    