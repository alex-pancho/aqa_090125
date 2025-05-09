from pages.elements import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    locators = {}

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def item(self, name: str) -> WebElement:
        _xpath = self.locators.get(name) # self.__getattribute__(name)
        msg = f"{self.__class__.__name__} has no xpath " + \
              f"for element: {name}, " + \
              f"may be typo? Exsist names is: {self.locators.keys()}"
        if _xpath is None:
            raise AttributeError(msg)
        return WebElement(driver=self.driver, xpath=_xpath)