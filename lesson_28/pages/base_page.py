from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def item(self, locator):
        """Пошук елемента за локатором."""
        return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def click(self, locator):
        """Клік на елемент."""
        self.item(locator).click()

    def send_keys(self, locator, keys):
        """Відправка тексту до елемента."""
        self.item(locator).send_keys(keys)

    def is_visible(self, locator):
        """Перевірка видимості елемента."""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
