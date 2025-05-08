from selenium.webdriver.common.by import By

class SignInPage:

    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.driver.get(url)
        if "Login Example" not in driver.title:
            raise ValueError(
                "This is not Sign In Page, current page is: " +
                driver.current_url)

    username_by = (By.NAME, "email")
    password_by = (By.NAME, "password")
    signin_by = (By.XPATH, '//form//div[.="Login"]')

    def login_valid_user(self, username, password):
        self.driver.find_element(*self.username_by).send_keys(username)
        self.driver.find_element(*self.password_by).send_keys(password)
        self.driver.find_element(*self.signin_by).click()
        return HomePage(self.driver)


class HomePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    message_by = (By.TAG_NAME, "h2")

    def get_message_text(self):
        return self.driver.find_element(*self.message_by).text