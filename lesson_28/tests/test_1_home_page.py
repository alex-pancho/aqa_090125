import pytest
from pages.home_page import HomePage

def test_homepage_menu(home_page):
    element = home_page.item("menu_home")
    assert element.is_visible(), f"Not found: {element._locator}"
    # element.highlight_and_make_screenshot("menu_home.png")


def test_homepage_sign_in(home_page):
    element = home_page.item("sign_in_button")
    assert element.is_visible(), f"Not found: {element._locator}"


def test_fail_path(home_page):
    with pytest.raises(AttributeError):
        element = home_page.item("add_car")
        element.is_visible()


def test_login_as_guest(driver, garage_page):
    guest_login = HomePage(driver).item("guest_login")
    assert guest_login.is_clickable()
    guest_login.click()
    assert garage_page.item("add_car").is_visible()

