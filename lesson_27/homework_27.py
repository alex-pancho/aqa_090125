from selenium import webdriver
from selenium.webdriver.common.by import By

class TrackNewPost:
    def __init__(self, tracking_number):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.tracking_number = tracking_number

    def open_page_track_info(self):
        """ Open page to search parcels"""
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def input_tracking_number(self):
        """ Enters tracking number and clicks the button "Пошук" """
        input_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
        input_field.send_keys(self.tracking_number)

        search_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        search_button.click()

    def get_status_text(self):
        """ Gets the status of parcel """
        search_result_element = self.driver.find_element(By.CLASS_NAME, "header__status-text")
        return search_result_element.text.strip()

    def close(self):
        """ Closes the browser """
        self.driver.quit()

# Тест функціональності
def test_tracking_status(tracking_number, expected_text):
    search_ttn = TrackNewPost(tracking_number)
    search_ttn.open_page_track_info()
    search_ttn.input_tracking_number()
    actual_text = search_ttn.get_status_text()
    search_ttn.close()

    assert actual_text == expected_text, f"Текст, що очікували: '{expected_text}', натомість отримано: '{actual_text}'"

# Виконання тесту
if __name__ == "__main__":
    test_tracking_status("20400454323503", "Відправлення отримано. Грошовий переказ видано одержувачу.")
    print("Результат проведення тесту - Успішно")