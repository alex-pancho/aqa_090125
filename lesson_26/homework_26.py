from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() # створили об'єкт driver

url_hw = "http://localhost:8000/dz.html"

driver.get(url_hw)

driver.switch_to.frame("frame1")
input_field_frame_1 = driver.find_element(By.ID, "input1")
input_field_frame_1.send_keys("Frame1_Secret")
check_button_frame_1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
check_button_frame_1.click()

time.sleep(3)
alert_msg_frame_1 = Alert(driver)
assert "Верифікація пройшла успішно!" in alert_msg_frame_1.text, "Введено неправильний текст!"
alert_msg_frame_1.accept()

driver.switch_to.default_content()

driver.switch_to.frame("frame2")
input_field_frame_2 = driver.find_element(By.ID, "input2")
input_field_frame_2.send_keys("Frame2_Secret")
check_button_frame_2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
check_button_frame_2.click()

time.sleep(3)
alert_msg_frame_2 = Alert(driver)
assert "Верифікація пройшла успішно!" in alert_msg_frame_2.text, "Введено неправильний текст"
alert_msg_frame_2.accept()

driver.quit()