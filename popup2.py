from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.ID, "name").send_keys("Pranabesh")

driver.find_element(By.ID, "alertbtn").click()

alert = Alert(driver)

print(alert.text)

alert.accept()

time.sleep(10)

driver.quit()