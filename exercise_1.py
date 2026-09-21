from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service       # for edge
# from selenium.webdriver.chrome.service import Service       # for chrome
import time

service_obj = Service()
driver = webdriver.Edge(options=options, service=service_obj)

driver.maximize_window()

# Browser open and access
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "btn1").click()
time.sleep(2)
driver.find_element(By.ID, "firstName").send_keys("Suyab Amin")
driver.find_element(By.ID, "lastName").send_keys("Sunny")
driver.find_element(By.ID, "userEmail").send_keys("syabbbbam@gmail.com")
driver.find_element(By.ID, "userMobile").send_keys("1745762524")
driver.find_element(By.CLASS_NAME, "custom-select").send_keys("Doctor")
driver.find_element(By.CLASS_NAME, "mt-3").click()
driver.find_element(By.ID, "userPassword").send_keys("Sa205158@#")
driver.find_element(By.ID, "confirmPassword").send_keys("Sa205158@#")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

driver.find_element(By.ID, "login").click()

time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn").click()


driver.find_element(By.CLASS_NAME, "form-control").send_keys("syabbbbam@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Sa205158@#")
driver.find_element(By.ID, "login").click()
driver.find_element(By.CLASS_NAME, "fa").click()
