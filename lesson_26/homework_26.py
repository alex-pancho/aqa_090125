from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def enter_text_and_click(driver, frame_id, input_id, secret_text):
    print(f"Переключення до фрейму: {frame_id}")
    driver.switch_to.default_content()
    driver.switch_to.frame(frame_id)
    print(f"Введення тексту '{secret_text}' у поле: {input_id}")
    input_element = driver.find_element(By.ID, input_id)
    input_element.send_keys(secret_text)
    button = driver.find_element(By.TAG_NAME, "button")
    print("Натискання кнопки 'Перевірити'")
    button.click()

def verify_alert(driver, expected_text, frame_id):
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"{frame_id} Alert text: {alert_text}")
        assert alert_text == expected_text, f"{frame_id} verification failed"
        alert.accept()
    except Exception as e:
        raise Exception(f"Помилка при роботі з alert у фреймі {frame_id}: {e}")
    finally:
        driver.switch_to.default_content()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:8000/dz.html")
        enter_text_and_click(driver, "frame1", "input1", "Frame1_Secret")
        verify_alert(driver, "Верифікація пройшла успішно!", "frame1")
        enter_text_and_click(driver, "frame2", "input2", "Frame2_Secret")
        verify_alert(driver, "Верифікація пройшла успішно!", "frame2")
        print("Всі фрейми пройшли верифікацію успішно.")
        time.sleep(2)
    finally:
        driver.quit()
