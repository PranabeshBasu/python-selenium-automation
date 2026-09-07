from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.ID, "name").send_keys("Pranabesh")

alert_button = driver.find_element(By.ID, "alertbtn")
alert_button.click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()

time.sleep(3)

driver.quit()