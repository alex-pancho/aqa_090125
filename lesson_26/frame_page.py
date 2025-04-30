from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class FramePage:
    def __init__(self, driver):
        self.url = "http://localhost:8000/dz.html"
        self.driver = driver
        self.alert = Alert(self.driver)

    frame_1_block = (By.XPATH, "//iframe[@id='frame1']")
    frame_2_block = (By.XPATH, "//iframe[@id='frame2']")

    frame_1_input = (By.XPATH, "//input[@id='input1']")
    frame_2_input = (By.XPATH, "//input[@id='input2']")

    frame_1_verify_button = (By.XPATH, "//button[contains(@onclick, 'input1')]")
    frame_2_verify_button = (By.XPATH, "//button[contains(@onclick, 'input2')]")

    def open_page(self):
        self.driver.get(self.url)

    def switch_to_frame(self, frame: tuple):
        frame = self.driver.find_element(*frame)
        self.driver.switch_to.frame(frame)

    def fill_field(self, text, field: tuple):
        self.driver.find_element(*field).send_keys(text)

    def click_verify_button(self, button: tuple):
        self.driver.find_element(*button).click()

    def verify_alert_text_and_close(self, text):
        assert self.alert.text == text, f"Wrong alert text. exp = {text}, actual = {self.alert.text}"
        self.alert.accept()
