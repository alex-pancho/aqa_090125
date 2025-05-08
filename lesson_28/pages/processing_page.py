
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProcessingPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, time_for_wait=5):
        """Функція для очікування наявності елемента на сторінці"""
        try:
            element = WebDriverWait(self.driver, timeout=time_for_wait).until(
                EC.presence_of_element_located((locator))
            )
            return element
        except TimeoutException:
            raise TimeoutException(
                f"Element with {locator} not found on {self.driver.current_url} during {time_for_wait} sec"
            )

    def wait_element_is_clickable(self, locator, time_for_wait=5):
        """Функція для очікування клiкабельностi елемента"""
        try:
            element = WebDriverWait(self.driver, timeout=time_for_wait).until(
                EC.element_to_be_clickable((locator))
            )
            return element

        except TimeoutException:
            raise TimeoutException(
                f"Element with {locator} is not visible and enabled such that you can click it"
                f" on {self.driver.current_url} during {time_for_wait} sec"
            )

    def click_element(self, locator):
        """Функція для кліку на елемент"""
        element = self.wait_element_is_clickable(locator)
        element.click()

    def fill_input(self, locator, text):
        """Функція для заповнення поля вводу текстом"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
