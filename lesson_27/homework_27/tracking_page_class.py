from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TrackingPage:
    """
    A class representing a tracking page in a web application.
    This class provides methods to interact with the page elements.
    """

    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self, url: str):
        """Open the page with the given URL."""
        self.driver.get(url)

    def find_element(self, xpath: str, timeout: int = 10):
        """Find an element on the page using its XPath."""
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except TimeoutException:
            raise TimeoutException (f"Element with {xpath} not found on {self.driver.current_url} during {timeout} sec")
    
    def fill_input(self, xpath: str, text: str):
        """Fill an input field with the given text. 
        Using the find_element method.
        """
        element = self.find_element(xpath)
        element.clear()
        element.send_keys(text)

    def wait_for_element_to_be_clickable(self, xpath: str, timeout: int = 10):
        """Wait for an element to be clickable."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element with {xpath} not clickable on {self.driver.current_url} during {timeout} sec")

    def click_button(self, xpath: str):
        """Click a button identified by its XPath. 
        Using the wait_for_element_to_be_clickable method.
        """
        element = self.wait_for_element_to_be_clickable(xpath)
        element.click()
