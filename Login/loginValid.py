from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa-interview.srcli.xyz/login")
driver.find_element(By.NAME, 'username').send_keys("root")
driver.find_element(By.NAME, 'password').send_keys("root123")
driver.find_element(By.XPATH, '/html/body/form/input[3]').click()
