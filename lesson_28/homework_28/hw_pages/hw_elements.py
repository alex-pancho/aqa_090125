from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElement:
    """This class provides methods to interact with the page elements."""

    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self, url: str):
        """Open the page with the given URL."""
        print(type(self.driver))
        self.driver.get(url)

    def find_element(self, locator, timeout: int = 10):
        """Find an element on the page using its XPath."""
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located((locator))
            )
            return element
        except TimeoutException:
            raise TimeoutException (f"Element with {locator} not found on {self.driver.current_url} during {timeout} sec")
    
    def fill_input(self, locator, text: str):
        """Fill an input field with the given text. 
        Using the find_element method.
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element_to_be_clickable(self, locator, timeout: int = 10):
        """Wait for an element to be clickable."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((locator))
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element with {locator} not clickable on {self.driver.current_url} during {timeout} sec")

    def click_button(self, locator):
        """Click a button identified by its XPath. 
        Using the wait_for_element_to_be_clickable method.
        """
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()
