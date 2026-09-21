from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service       # for edge
# from selenium.webdriver.chrome.service import Service       # for chrome
import time

options = webdriver.EdgeOptions()
service_obj = Service()
driver = webdriver.Edge(options=options, service=service_obj)

driver.maximize_window()

# Browser open and access
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

elements = driver.find_elements(By.CLASS_NAME, "tableFixHead")
time.sleep(5)
for E in elements:
    print(E.text)
    # Assert
assert "Ben" in elements[0].text

print("Assertion passed!")
input("Press Enter only when you want to finish...")