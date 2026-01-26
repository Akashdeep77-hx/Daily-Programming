from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time 
from trio import sleep


# Start Chrome driver
driver = webdriver.Chrome(service=Service("C:\\Windows\\chromedriver.exe"))

# Open website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Enter username
driver.find_element(By.NAME, "username").send_keys("Admin")

# Enter password automate
driver.find_element(By.NAME, "password").send_keys("admin123")

# Click Login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#To close browser
driver.close()































