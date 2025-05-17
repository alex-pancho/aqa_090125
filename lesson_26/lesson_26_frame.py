from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://localhost/frame.html")

text_on_page = driver.find_element(By.XPATH, '//*[@id="myid"]')
# print(text_on_page.is_displayed())
text_on_page.click()
# driver.execute_script("window.scrollTo(0, 0);")
# Перемикаємося до фрейму
# youtube = driver.find_element(By.XPATH,'//*[@title="YouTube video player"]')
# print(youtube.is_displayed())
driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))
youtube = driver.find_element(By.XPATH,'//*[@title="YouTube video player"]')
print(youtube.is_displayed())
driver.switch_to.default_content()
