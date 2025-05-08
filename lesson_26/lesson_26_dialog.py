from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()

driver.get("http://localhost/dialog.html")

driver.find_element(By.XPATH, "//button[text()='Показати Alert']").click()
alert = Alert(driver)
print("Текст Alert:", alert.text)
alert.accept()

# Показати Confirm і підтвердити його
driver.find_element(By.XPATH, "//button[.='Показати Confirm']").click()
alert = Alert(driver)
print("Текст Confirm:", alert.text)
alert.accept()

# Показати Prompt, ввести текст і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
alert = Alert(driver)
print("Текст Prompt:", alert.text)
alert.send_keys("John")
alert.accept()

