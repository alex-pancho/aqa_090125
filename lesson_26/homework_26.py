from selenium import webdriver
from selenium.webdriver.common.by import By
import time


frames_secrets = {
        "frame1": ("input1", "Frame1_Secret"),
        "frame2": ("input2", "Frame2_Secret"),
    }
def verify_frame(driver, frame_id, input_id, secret_text):
        
        # Переходимо у фрейм
        frame = driver.find_element(By.ID, frame_id)
        driver.switch_to.frame(frame)

        # Вводимо текст
        input_field = driver.find_element(By.ID, input_id)
        input_field.send_keys(secret_text)

        # Натискаємо кнопку
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        # Чекаємо на alert
        for _ in range(10):
            try:
                alert = driver.switch_to.alert
                break
            except:
                time.sleep(0.5)
            else:
                raise Exception(f"❌ Алерт не з'явився у {frame_id}")

        # Отримуємо alert і перевіряємо текст
        alert = driver.switch_to.alert
        print(f"{frame_id} alert: {alert.text}")
        assert alert.text == "Верифікація пройшла успішно", f"Помилка у {frame_id}"
        alert.accept()

        driver.switch_to.default_content()
        time.sleep(1)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/dz.html")

    for frame_id, (input_id, secret) in frames_secrets.items():
        verify_frame(driver, frame_id, input_id, secret)

    print("Верифікація усіх фреймів пройшла успішно")
    driver.quit()