from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

driver.get("http://localhost")

user_field = driver.find_element(By.ID, "username")
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")
li_elements = driver.find_elements(By.TAG_NAME, "li")
# user_field = driver.find_element(By.XPATH, "//input[@id='username']")
# pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
# log_button = driver.find_element(By.XPATH, "//button[@id='login_button']")
user_field.send_keys("Hello world!")
for li in li_elements:
    print("Знайдено елемент:", li.text)

login_button.click()

driver.get("http://localhost/demo.html")
# Знаходження текстових полів за ID і введення тексту
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("example_username")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("example_password")

male_radio = driver.find_element(By.ID, "male")
male_radio.click()

newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()

# Вибір значення з випадаючого списку за ID
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("США")
# country_dropdown.select_by_value("usa")

#driver.quit()

