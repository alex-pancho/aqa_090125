from get_browser import firefox, chrome
from first_po_class import SignInPage


LOGIN_URL = "https://semantic-ui.com/examples/login.html"

def test_login():
    driver = firefox(True)
    sign_in = SignInPage(driver, LOGIN_URL)
    assert sign_in.driver is not None
    user = "user@gmail.com"
    password = "my supersecret password"
    afrer_login = sign_in.login_valid_user(user, password)
    assert afrer_login.get_message_text() == "Log-in to your account"
    driver.close()