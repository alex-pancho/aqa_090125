import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def send_text_into_frame(driver, frame_id, input_id, text):
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))

    driver.find_element(By.ID, input_id).send_keys(text)
    
    button = driver.find_element(By.TAG_NAME, "button")
    time.sleep(1)
    button.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    assert alert.text == "Верифікація пройшла успішно!", f"Невірний текст алерта: {alert.text}"
    alert.accept()
    time.sleep(3)

    driver.switch_to.default_content()



if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/dz.html")
    send_text_into_frame(driver, "frame1", "input1", "Frame1_Secret")
    send_text_into_frame(driver, "frame2", "input2", "Frame2_Secret")
    driver.quit()
