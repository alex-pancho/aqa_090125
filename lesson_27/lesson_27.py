# EXplicit for EXpected
# IMplicit for IMaginary
from selenium import webdriver
from domelement import webelement, get_element_with_text_value


def test_example_with_implicit_wait(driver):
    driver.implicitly_wait(10)  # Чекати не більше 10 секунд
    driver.get("https://www.example.com")
    # Знаходимо елемент на сторінці
    heading = driver.find_element_by_tag_name("h1")
    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.example.com")
    xpath = '//li[@id="ewuygeb"]' #  '//p/a'
    # element = webelement(driver, xpath, 1)
    # element.click()
    element = get_element_with_text_value(driver, '//p/a', "More", 1)
    # Закриття браузера
    driver.quit()
