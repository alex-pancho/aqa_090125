from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def switch_to_frame_by_xpath(driver, frame_xpath):
    """Перемикається на вказаний фрейм за його XPath."""
    print(f"Перехід до фрейму з XPath: {frame_xpath}")
    frame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, frame_xpath))
    )
    driver.switch_to.frame(frame)

def enter_secret_text_by_xpath(driver, input_xpath, secret_text):
    """Вводить секретний текст у вказане поле вводу за його XPath."""
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, input_xpath))
    )
    input_field.send_keys(secret_text)
    print(f"Введено текст: '{secret_text}' у поле з XPath: {input_xpath}")

def click_verify_button_by_xpath(driver, verify_button_xpath):
    """Натискає кнопку 'Перевірити' за її XPath."""
    verify_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, verify_button_xpath))
    )
    verify_button.click()
    print("Натиснуто кнопку 'Перевірити'")

def handle_verification_alert(driver):
    """Очікує, перевіряє та приймає діалогове вікно підтвердження."""
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == SUCCESS_ALERT_TEXT, f"Отримано невірний текст підтвердження: '{alert_text}', очікувалось: '{SUCCESS_ALERT_TEXT}'"
    print(f"Текст діалогового вікна: '{alert_text}' - верифікація успішна.")
    alert.accept()
    print("Діалогове вікно закрито.")

if __name__ == "__main__":

    # XPath локатори елементів
    FRAME_1_XPATH = "//iframe[@id='frame1']"
    FRAME_2_XPATH = "//iframe[@id='frame2']"
    INPUT_1_XPATH = "//input[@id='input1']"
    INPUT_2_XPATH = "//input[@id='input2']"
    VERIFY_BUTTON_XPATH = "//button[text()='Перевірити']"
    SUCCESS_ALERT_TEXT = "Верифікація пройшла успішно!"

    driver = webdriver.Firefox()
    driver.get("http://localhost:8000/dz.html")

    # Верифікація першого фрейму
    switch_to_frame_by_xpath(driver, FRAME_1_XPATH)
    enter_secret_text_by_xpath(driver, INPUT_1_XPATH, "Frame1_Secret")
    click_verify_button_by_xpath(driver, VERIFY_BUTTON_XPATH)
    handle_verification_alert(driver)
    driver.switch_to.default_content()

    # Верифікація другого фрейму
    switch_to_frame_by_xpath(driver, FRAME_2_XPATH)
    enter_secret_text_by_xpath(driver, INPUT_2_XPATH, "Frame2_Secret")
    click_verify_button_by_xpath(driver, VERIFY_BUTTON_XPATH)
    handle_verification_alert(driver)
    driver.switch_to.default_content()

    print("Успішно пройдено верифікацію в обох фреймах.")
    driver.quit()


   