from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def webelement(driver, xpath, time_for_wait:int = 5):
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element with {xpath} not found on {driver.current_url} during {time_for_wait} sec")


def visibility(driver, xpath, time_for_wait:int = 5):
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element with {xpath} not visibl on {driver.current_url} during {time_for_wait} sec")


def clickable(driver, xpath, time_for_wait:int = 5):
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element with {xpath} not click on {driver.current_url} during {time_for_wait} sec")


class ElementTextContains:
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        try:
            element = driver.find_element(By.XPATH, self.locator)
            return self.text in element.text
        except:
            return False


def get_element_with_text_value(driver, xpath:str, text_value:str, max_timeout:int = 10):
    wait = WebDriverWait(driver, max_timeout)

    try:
        return wait.until(ElementTextContains(xpath, text_value))
    except:
        raise TimeoutException(f"Element")


def click_element(driver, xpath):
    """Функція для кліку на елемент"""
    element = clickable(driver, xpath)
    element.click()


def fill_input(driver, xpath, text):
    """Функція для заповнення поля вводу текстом"""
    element = webelement(driver, xpath)
    element.clear()
    element.send_keys(text)